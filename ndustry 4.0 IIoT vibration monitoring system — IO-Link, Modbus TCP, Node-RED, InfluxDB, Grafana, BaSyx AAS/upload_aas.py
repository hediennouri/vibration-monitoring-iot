import urllib.request, json

BASYX_URL = "http://localhost:4001"

def post(endpoint, data):
    url = f"{BASYX_URL}/{endpoint}"
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode(),
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    try:
        resp = urllib.request.urlopen(req)
        print(f"OK: {url}")
        return True
    except Exception as e:
        err = e.read().decode() if hasattr(e, "read") else str(e)
        if "already exists" in err or "Conflict" in err:
            print(f"Already exists (skipping): {url}")
            return True
        print(f"Error: {err}")
        return False

# ── 1. AAS Shell ──────────────────────────────────────────────────────────────
print("\n--- Uploading AAS Shell ---")
post("shells", {
    "idShort": "VibrationBenchAAS",
    "id": "urn:ipcb:aas:vibration-bench:001",
    "assetInformation": {
        "assetKind": "Instance",
        "globalAssetId": "urn:ipcb:asset:schmidt-lgea63:001"
    },
    "submodels": [
        {"type": "ExternalReference", "keys": [{"type": "Submodel", "value": "urn:ipcb:sm:identification:001"}]},
        {"type": "ExternalReference", "keys": [{"type": "Submodel", "value": "urn:ipcb:sm:technicaldata:001"}]},
        {"type": "ExternalReference", "keys": [{"type": "Submodel", "value": "urn:ipcb:sm:monitoring:001"}]}
    ]
})

# ── 2. Identification Submodel ────────────────────────────────────────────────
print("\n--- Uploading Identification Submodel ---")
post("submodels", {
    "idShort": "Identification",
    "id": "urn:ipcb:sm:identification:001",
    "submodelElements": [
        {"idShort": "Manufacturer",   "modelType": "Property", "valueType": "xs:string", "value": "Schmidt Industrie Elektronik"},
        {"idShort": "MotorModel",     "modelType": "Property", "valueType": "xs:string", "value": "LGEA 63"},
        {"idShort": "SerialNumber",   "modelType": "Property", "valueType": "xs:string", "value": "423"},
        {"idShort": "SensorModel",    "modelType": "Property", "valueType": "xs:string", "value": "Turck CMVT-QR20-IOLX3-0.3-RS4"},
        {"idShort": "IOLinkMaster",   "modelType": "Property", "valueType": "xs:string", "value": "Turck TBEN-S2-4IOL"},
        {"idShort": "Location",       "modelType": "Property", "valueType": "xs:string", "value": "Vibration Test Bench - IPCB Lab"}
    ]
})

# ── 3. TechnicalData Submodel ─────────────────────────────────────────────────
print("\n--- Uploading TechnicalData Submodel ---")
post("submodels", {
    "idShort": "TechnicalData",
    "id": "urn:ipcb:sm:technicaldata:001",
    "submodelElements": [
        {"idShort": "RatedPower_kW",       "modelType": "Property", "valueType": "xs:double", "value": "0.2"},
        {"idShort": "RatedSpeed_rpm",      "modelType": "Property", "valueType": "xs:int",    "value": "3000"},
        {"idShort": "Voltage_V",           "modelType": "Property", "valueType": "xs:string", "value": "160/200"},
        {"idShort": "Current_A",           "modelType": "Property", "valueType": "xs:string", "value": "1.6/0.22"},
        {"idShort": "InsulationClass",     "modelType": "Property", "valueType": "xs:string", "value": "F"},
        {"idShort": "ProtectionClass",     "modelType": "Property", "valueType": "xs:string", "value": "IP44"},
        {"idShort": "MaxWindingTemp_C",    "modelType": "Property", "valueType": "xs:int",    "value": "155"},
        {"idShort": "VibrationRange",      "modelType": "Property", "valueType": "xs:string", "value": "+-16 g"},
        {"idShort": "VibrationResolution", "modelType": "Property", "valueType": "xs:string", "value": "0.01 g"},
        {"idShort": "TemperatureRange",    "modelType": "Property", "valueType": "xs:string", "value": "-40 to 85 C"},
        {"idShort": "Protocol",            "modelType": "Property", "valueType": "xs:string", "value": "IO-Link COM3 230.4kBaud"}
    ]
})

# ── 4. Monitoring Submodel ────────────────────────────────────────────────────
print("\n--- Uploading Monitoring Submodel ---")
post("submodels", {
    "idShort": "Monitoring",
    "id": "urn:ipcb:sm:monitoring:001",
    "submodelElements": [
        {"idShort": "VibrationWarning_g",       "modelType": "Property", "valueType": "xs:double", "value": "2.3"},
        {"idShort": "VibrationAlarm_g",         "modelType": "Property", "valueType": "xs:double", "value": "4.5"},
        {"idShort": "TemperatureWarning_C",     "modelType": "Property", "valueType": "xs:double", "value": "80.0"},
        {"idShort": "TemperatureAlarm_C",       "modelType": "Property", "valueType": "xs:double", "value": "100.0"},
        {"idShort": "Standard",                 "modelType": "Property", "valueType": "xs:string", "value": "ISO 10816 - small machines under 15kW"},
        {"idShort": "KPI_VibrationRMS",         "modelType": "Property", "valueType": "xs:string", "value": "RMS amplitude in g"},
        {"idShort": "KPI_PeakVibration",        "modelType": "Property", "valueType": "xs:string", "value": "Max vibration in last 1 hour"},
        {"idShort": "KPI_AverageVibration",     "modelType": "Property", "valueType": "xs:string", "value": "Mean vibration over last 5 minutes"},
        {"idShort": "KPI_MotorTemperature",     "modelType": "Property", "valueType": "xs:string", "value": "Surface temperature in Celsius"},
        {"idShort": "DataPipeline",             "modelType": "Property", "valueType": "xs:string", "value": "TBEN-S2-4IOL > Modbus TCP > Node-RED > InfluxDB > Grafana"},
        {"idShort": "Dashboard",                "modelType": "Property", "valueType": "xs:string", "value": "http://localhost:3000"},
        {"idShort": "AAS_Server",               "modelType": "Property", "valueType": "xs:string", "value": "http://localhost:4001"}
    ]
})

print("\nDone! Check http://localhost:4001/shells and http://localhost:3001")
