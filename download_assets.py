"""Optional: download MediaPipe runtime + models so the app works 100% offline.
Run once:  python download_assets.py
index.html automatically prefers these local files and falls back to the CDN if missing.
"""
import os
import urllib.request

VER = "0.10.14"
CDN = f"https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@{VER}"
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")

FILES = {
    "vendor/tasks-vision/vision_bundle.mjs": f"{CDN}/vision_bundle.mjs",
    "vendor/tasks-vision/wasm/vision_wasm_internal.js": f"{CDN}/wasm/vision_wasm_internal.js",
    "vendor/tasks-vision/wasm/vision_wasm_internal.wasm": f"{CDN}/wasm/vision_wasm_internal.wasm",
    "vendor/tasks-vision/wasm/vision_wasm_nosimd_internal.js": f"{CDN}/wasm/vision_wasm_nosimd_internal.js",
    "vendor/tasks-vision/wasm/vision_wasm_nosimd_internal.wasm": f"{CDN}/wasm/vision_wasm_nosimd_internal.wasm",
    "models/face_landmarker.task": "https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task",
    "models/pose_landmarker_full.task": "https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_full/float16/1/pose_landmarker_full.task",
    "models/hand_landmarker.task": "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task",
}

THREE = "https://cdn.jsdelivr.net/npm/three@0.160.0"
FILES.update({
    "vendor/three/three.module.js": f"{THREE}/build/three.module.js",
    "vendor/three/addons/loaders/GLTFLoader.js": f"{THREE}/examples/jsm/loaders/GLTFLoader.js",
    "vendor/three/addons/utils/BufferGeometryUtils.js": f"{THREE}/examples/jsm/utils/BufferGeometryUtils.js",
})

for rel, url in FILES.items():
    dst = os.path.join(BASE, rel)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if os.path.exists(dst) and os.path.getsize(dst) > 0:
        print("✓ exists  ", rel)
        continue
    print("↓", rel)
    urllib.request.urlretrieve(url, dst)
print("Done. Start the app with: python app.py")
