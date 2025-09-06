# 2D → 3D Converter

This project provides a **responsive web app** that converts 2D images into interactive 3D models. It consists of a React frontend and a Python backend.

---

## Features
- 📤 Upload any 2D image
- ⚙️ Choose conversion method (depth-mesh, neural, experimental NeRF)
- 🖼 Preview uploaded image
- 🌀 Real-time 3D model viewer (rotating preview)
- 📜 Conversion logs panel
- 📱 Fully responsive design (desktop & mobile)

---

## Project Structure
```
2d_to_3d_converter/
│
├── frontend/             # React app (UI)
│   └── 2DTo3DApp.jsx
│
├── backend/              # Flask API (conversion pipeline)
│   └── server.py
│
└── README.md             # Documentation
```

---

## Frontend (React)
- Written in **React + TailwindCSS**
- Uses **Three.js** with `GLTFLoader` for 3D preview
- Responsive grid layout for input panel & viewer

### Run Frontend
```bash
cd frontend
npm install
npm run dev
```

---

## Backend (Flask)
- Exposes `/api/convert` endpoint
- Accepts uploaded image
- Runs depth → point cloud → mesh → glTF export pipeline
- Returns `modelUrl` pointing to the generated 3D model

### Run Backend
```bash
cd backend
pip install -r requirements.txt
python server.py
```

---

## Example Workflow
1. Start backend (`python server.py`)
2. Start frontend (`npm run dev`)
3. Open `http://localhost:5173/`
4. Upload image → wait for conversion → preview model in 3D

---

## Requirements
- **Frontend:** Node.js 18+
- **Backend:** Python 3.9+
- **Libraries:** Flask, Open3D, MiDaS (PyTorch), Trimesh
- **Optional:** GPU for faster inference

---

## Roadmap
- [ ] Multi-image support for better reconstruction
- [ ] Dockerfile for easy deployment
- [ ] Export formats (OBJ, FBX)
- [ ] Advanced controls (zoom, pan, orbit)

---

## License
MIT — Free to use and modify.

---

✨ Built with React, Flask, and Three.js
