# 🏭 Industrial Vibration Monitoring System — Industry 4.0

> A complete IIoT condition monitoring system built on a vibration test bench, implementing a full Industry 4.0 architecture from sensor to digital asset representation.

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Node-RED](https://img.shields.io/badge/Node--RED-8F0000?style=flat&logo=nodered&logoColor=white)
![InfluxDB](https://img.shields.io/badge/InfluxDB-22ADF6?style=flat&logo=influxdb&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat&logo=grafana&logoColor=white)
![BaSyx](https://img.shields.io/badge/Eclipse_BaSyx-2C2255?style=flat&logo=eclipse&logoColor=white)

---

## 📋 Overview

This project implements a real-time vibration and temperature monitoring system for an industrial motor, following Industry 4.0 principles. It integrates hardware-level sensor communication with a full software pipeline for data storage, visualization, alerting, and digital asset representation.

The system was developed as part of the **Industrial Systems in the Digital Era** course at **Escola Superior de Tecnologia — Instituto Politécnico de Castelo Branco**.

---

## 🏗️ Architecture

```
Vibration Sensor (CMVT-QR20)
        │ IO-Link
        ▼
TBEN-S2-4IOL IO-Link Master
        │ Modbus TCP (port 502)
        ▼
Node-RED  ──────────────────► InfluxDB (time-series DB)
        │                            │
        │                            ▼
        │                       Grafana Dashboard
        │                       (KPIs + Alerts)
        ▼
Eclipse BaSyx AAS Server
(Digital Asset Representation)
```

---

## 🔧 Hardware Used

| Component | Model | Role |
|---|---|---|
| Motor | Schmidt LGEA 63 (0.2kW, 3000rpm) | Asset under monitoring |
| Vibration/Temp Sensor | Turck CMVT-QR20-IOLX3-0.3-RS4 | Data acquisition |
| IO-Link Master | Turck TBEN-S2-4IOL | Protocol conversion (IO-Link → Modbus TCP) |

---

## 💻 Software Stack

| Service | Technology | Port |
|---|---|---|
| Data pipeline | Node-RED | 1880 |
| Time-series DB | InfluxDB 2.7 | 8086 |
| Dashboard | Grafana 10.4.2 | 3000 |
| AAS Server | Eclipse BaSyx v2 | 4001 |
| AAS GUI | Eclipse BaSyx UI | 3001 |

All services run in **Docker containers** via docker-compose.

---

## 📊 Features

- ✅ Real-time vibration and temperature data acquisition via IO-Link + Modbus TCP
- ✅ Live Grafana dashboard with 6 KPI panels
- ✅ ISO 10816-based alert rules (vibration warning, critical, temperature warning)
- ✅ Asset Administration Shell (AAS) with 3 submodels (Identification, TechnicalData, Monitoring)
- ✅ Full Docker containerization
- ✅ Time-series data storage with InfluxDB

---

## 📈 KPIs Monitored

| KPI | Unit | Description |
|---|---|---|
| Vibration RMS (current) | g | Instantaneous acceleration amplitude |
| Vibration average | g | Mean over last 5 minutes |
| Vibration peak | g | Maximum over last hour |
| Motor temperature | °C | Surface temperature |
| Vibration severity | 0–3 | ISO 10816 zone classification |

---

## 🚨 Alert Thresholds (ISO 10816 — Class I machines)

| Alert | Threshold | ISO 10816 Zone |
|---|---|---|
| Vibration Warning | > 2.3 g | Zone C — restricted operation |
| Vibration Critical | > 4.5 g | Zone D — risk of damage |
| Temperature Warning | > 80 °C | Approaching Class F insulation limit |

---

## 🚀 How to Run

### Prerequisites
- Docker Desktop installed and running
- Python 3.x
- Node-RED nodes: `node-red-contrib-modbus`, `node-red-contrib-influxdb`

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/vibration-monitoring-iot.git
cd vibration-monitoring-iot
```

### 2. Configure environment
Copy the example env file and edit credentials:
```bash
cp .env.example .env
```

### 3. Start all services
```bash
docker-compose up -d
```

Wait 2 minutes for all containers to initialize.

### 4. Import Node-RED flow
- Open http://localhost:1880
- Menu (☰) → Import → select `nodered_flows/flow.json`
- Click Deploy

### 5. Upload the AAS
```bash
python upload_aas.py
```

### 6. Access the interfaces

| Interface | URL | Credentials |
|---|---|---|
| Node-RED | http://localhost:1880 | — |
| InfluxDB | http://localhost:8086 | admin / see .env |
| Grafana | http://localhost:3000 | admin / admin |
| BaSyx AAS API | http://localhost:4001/shells | — |
| BaSyx AAS GUI | http://localhost:3001 | — |

---

## 📁 Repository Structure

```
vibration-monitoring-iot/
├── docker-compose.yml          # All services definition
├── upload_aas.py               # BaSyx AAS loader script
├── .env.example                # Environment variables template
├── .gitignore
├── README.md
├── nodered_flows/
│   └── flow.json               # Node-RED flow (import this)
├── grafana_provisioning/
│   ├── datasources/
│   │   └── influxdb.yml        # Auto-connects Grafana to InfluxDB
│   └── dashboards/
│       ├── dashboard.yml
│       └── vibration.json      # Pre-built dashboard
└── docs/
    └── report.pdf              # Full project report
```

---

## 🔐 Security Note

This project uses hardcoded credentials for local development only. For production use, replace all credentials with environment variables via the `.env` file and never commit secrets to Git.

---

## 📚 References

- [Turck CMVT-QR20 Datasheet](https://www.turck.com)
- [Turck TBEN-S2-4IOL Manual](https://www.turck.com)
- [Eclipse BaSyx Documentation](https://eclipse.dev/basyx/)
- [ISO 10816 Vibration Standard](https://www.iso.org)
- [Node-RED Documentation](https://nodered.org/docs/)
- [InfluxDB v2 Documentation](https://docs.influxdata.com/influxdb/v2/)

---

## 👤 Author

**Hedi Ennouri**  
Industrial Engineering and Management  
Escola Superior de Tecnologia — IPCB  
2025/2026
