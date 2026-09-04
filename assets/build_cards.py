import subprocess, urllib.parse, pathlib, os
from PIL import Image

HERE = pathlib.Path(__file__).parent.resolve()
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
CARD = (HERE / "card.html").as_uri()

CARDS = [
    dict(slug="casamotion", kicker="Real time data", title="CasaMotion",
         line="Rider matching for Casablanca in under 5 seconds, with demand forecast per district.",
         chips="Kafka,Flink,Spark,Cassandra", img="casa_crop.png", mode="", pos="center"),
    dict(slug="arya", kicker="AI agents", title="ARYA, multi-agent recruitment",
         line="Six LangGraph agents run a hiring pipeline end to end, deployed on Azure.",
         chips="LangGraph,FastAPI,Azure", img="arya.png", mode="pad", pos="center"),
    dict(slug="job-intelligent", kicker="Data platform", title="job-intelligent",
         line="Job matching for data roles. Bronze, Silver, Gold lakehouse, every score explained.",
         chips="Airflow,pgvector,React,Power BI", img="job.png", mode="pad", pos="center"),
    dict(slug="netix", kicker="Computer vision", title="Netix",
         line="Reads a router's LEDs through the phone camera and guides the customer to the fix.",
         chips="ONNX,OpenCV,FastAPI", img="netix_cam.png", mode="phone", pos="center"),
    dict(slug="procurement", kicker="Big data", title="Procurement data pipeline",
         line="Daily orders from 15 stores and 5 warehouses on HDFS, queried through Trino.",
         chips="Hadoop,Trino,Airflow", img="proc.png", mode="pad", pos="center"),
    dict(slug="aethersignal", kicker="Machine learning", title="AetherSignal",
         line="RNN, GRU, LSTM and XGBoost compete to predict large ETH moves from 48h of data.",
         chips="PyTorch,XGBoost,Streamlit", img="eth_crop.png", mode="phone", pos="center"),
]

for c in CARDS:
    params = dict(c); params["img"] = (HERE / "src" / c["img"]).as_uri()
    url = CARD + "?" + urllib.parse.urlencode(params)
    out = HERE / f"{c['slug']}.png"
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    "--window-size=1200,630", f"--screenshot={out}", url],
                   check=True, capture_output=True)
    im = Image.open(out).convert("RGB")
    im.save(out, optimize=True)
    print(c["slug"], im.size, os.path.getsize(out) // 1024, "KB")
