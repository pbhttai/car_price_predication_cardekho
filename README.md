## Car Price Predication from CarDekho

Dataset used from kaggle link: https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho

## How to Run the App
### Create virtual Environment
```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### Run this on terminal (same project root):
should be run on http://127.0.0.1:8000 or change your api url on streamlit_app.py
```bash
python -m uvicorn app.main:app --reload
```

### Open another terminal (same project root):
```bash
.\venv\Scripts\activate
python -m streamlit run app/streamlit_app.py
```

### Clone or Download the Project
```bash
git clone https://github.com/pbhttai/car_price_predication_cardekho.git
cd car_price_predication_cardekho
```
