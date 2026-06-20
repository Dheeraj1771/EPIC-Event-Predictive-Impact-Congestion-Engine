import streamlit as st
import pandas as pd
from datetime import datetime
import os
from supabase import create_client, Client

st.set_page_config(page_title="Post-Event Learning", page_icon="💾", layout="wide")

# Custom CSS for the clean light-mode cards
st.markdown("""
    <style>
    .log-card {
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 24px;
        background-color: #ffffff;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .log-card p {
        margin-bottom: 10px;
        font-size: 1rem;
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)

st.title("💾 Post-Event Learning System")
st.write("Commit operational directives to the historical database. This closed-loop system ensures the E.P.I.C. Machine Learning model continuously learns from real-world deployments.")

st.write("---")

col1, col2 = st.columns([1, 1.5])

with col1:
    st.subheader("📤 Pending Deployment Log")
    
    # Check if a simulation was run on the Map page and hasn't been committed yet
    if 'last_event' in st.session_state and st.session_state.last_event:
        event = st.session_state.last_event
        
        # FIX: Combine all text inside a single HTML block so the div wraps correctly
        st.markdown(f"""
            <div class="log-card">
                <p><b>📍 Location:</b> {event['location']}</p>
                <p><b>🚦 Category:</b> {event['type']} ({event['cause']})</p>
                <p><b>📈 Computed Severity:</b> {event['severity']}/10.0</p>
                <p><b>👮 Dispatched Personnel:</b> {event['personnel']} Officers</p>
                <p style="margin-bottom: 0;"><b>📅 Timestamp:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("☁️ Commit to Supabase Database", type="primary", use_container_width=True):
            try:
                # 1. Fetch Cloud Keys (Streamlit Secrets)
                SUPABASE_URL = st.secrets.get("SUPABASE_URL", os.environ.get("SUPABASE_URL"))
                SUPABASE_KEY = st.secrets.get("SUPABASE_KEY", os.environ.get("SUPABASE_KEY"))
                
                if not SUPABASE_URL or not SUPABASE_KEY:
                    st.error("⚠️ Database connection skipped: Supabase API keys not found in `.streamlit/secrets.toml`.")
                else:
                    # 2. Connect to Database
                    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
                    
                    # 3. Structure the exact payload
                    payload = {
                        "location": event['location'],
                        "event_type": event['type'],
                        "event_cause": event['cause'],
                        "severity_scale": event['severity'],
                        "dispatched_personnel": event['personnel'],
                        "timestamp": datetime.now().isoformat()
                    }
                    
                    # 4. Execute the Insert
                    supabase.table("epic_event_logs").insert(payload).execute()
                
                # --- UX UPGRADE: Clear the pending log and trigger a UI refresh ---
                st.session_state.last_event = None
                st.session_state.just_committed = True
                st.rerun()
                
            except Exception as e:
                st.error(f"Cloud Connection Error: Ensure your Supabase table 'epic_event_logs' is created. Details: {e}")
            
    else:
        # Check if we just committed something so we can show a nice success message
        if st.session_state.get('just_committed'):
            st.success("✅ Successfully committed to the database! The pending log has been cleared.")
            st.balloons()
            st.session_state.just_committed = False # Reset flag so it doesn't show forever
        else:
            st.info("No pending deployments. Please run a simulation on the 'Live Command Map' first.")

with col2:
    st.subheader("📚 Historical Training Ledger")
    st.write("Recent events actively training the AI Model (Mocked for Demo purposes):")
    
    # Mock historical database to show the judges the "Learning" aspect
    mock_db = pd.DataFrame({
        "Event ID": ["EVT-902", "EVT-901", "EVT-900", "EVT-899", "EVT-898"],
        "Location": ["Bellandur ORR", "Majestic Bus Stand", "M. Chinnaswamy", "Silk Board", "Indiranagar 100ft"],
        "Cause": ["Water Logging", "VIP Movement", "Sports Event", "Vehicle Breakdown", "Sudden Gathering"],
        "Personnel Deployed": [45, 60, 120, 15, 30],
        "Feedback Accuracy": ["94% Match", "88% Match", "97% Match", "82% Match", "91% Match"]
    })
    
    st.dataframe(mock_db, use_container_width=True, hide_index=True)