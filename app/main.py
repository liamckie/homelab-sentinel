from fastapi import FastAPI, HTTPException
from datetime import datetime, timezone
from fastapi.responses import HTMLResponse

latest_heartbeat = None
ONLINE_THRESHOLD = 30
OFFLINE_THRESHOLD = 60


app = FastAPI(
    title="Homelab Sentinel API",
    description="Monitoring and alerting API for homelab services",
    version="0.1.0",
)


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "homelab-sentinel-api",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


@app.get("/version")
def version():
    return {
        "name": "homelab-sentinel-api",
        "version": "0.1.0"
    }
    
    
@app.post("/heartbeat")
def heartbeat():
    global latest_heartbeat    

    latest_heartbeat = datetime.now(timezone.utc)

    return {
        "status": "received",
        "timestamp": latest_heartbeat.isoformat() if latest_heartbeat else None # Return the timestamp of the latest heartbeat if it exists
    }  
    
    
@app.get("/status", response_class=HTMLResponse)
def status():
    current_status = calculate_status()

    return f"""
    <html>
        <head>
            <title>Homelab Sentinel</title>
        </head>
        <body>
            <h1>Homelab Sentinel</h1>
            <p>Status: {current_status}</p>
            <p>Last heartbeat: {latest_heartbeat}</p>
        </body>
    </html>
    """ 
    

@app.get("/api/status")
def api_status():
    return {
        "status": calculate_status(),
        "latest_heartbeat": latest_heartbeat
    }    
    
    
# Helper function to calculate the overall status based on the latest heartbeat
def calculate_status():
    if latest_heartbeat is None:
        return "unknown"

    now = datetime.now(timezone.utc)

    age = (now - latest_heartbeat).total_seconds()

    if age <= ONLINE_THRESHOLD:
        return "online"

    if age <= OFFLINE_THRESHOLD:
        return "delayed"

    return "offline"    