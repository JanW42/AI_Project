import sys
import os
from pathlib import Path
from faster_whisper import WhisperModel
from settings import settings #Lokal eigene Lib
from icecream import ic

#pip install faster-whisper
#pip install pyaudio

def set_cuda_paths():
    venv_base = Path(sys.executable).parent.parent
    nvidia_base_path = venv_base / 'Lib' / 'site-packages' / 'nvidia'
    cuda_path = nvidia_base_path / 'cuda_runtime' / 'bin'
    cublas_path = nvidia_base_path / 'cublas' / 'bin'
    cudnn_path = nvidia_base_path / 'cudnn' / 'bin'
    paths_to_add = [str(cuda_path), str(cublas_path), str(cudnn_path)]
    env_vars = ['CUDA_PATH', 'CUDA_PATH_V12_4', 'PATH']
    
    for env_var in env_vars:
        current_value = os.environ.get(env_var, '')
        new_value = os.pathsep.join(paths_to_add + [current_value] if current_value else paths_to_add)
        os.environ[env_var] = new_value
    #print("CUDA_PFAD wurde erfolgreich gesetzt")
    
#pip install torch==2.6.0
#pip install torchaudio==2.6.0
#pip install nvidia-cudnn-cu12==9.5.0.50
#pip install nvidia-cuda-nvrtc-cu12==12.4.127
#pip install nvidia-cuda-runtime-cu12==12.4.127
#pip install nvidia-cublas-cu12==12.4.5.8

def speech_to_text_processer():
    model_size = settings.model_size

    # Run on GPU with FP16
    model = WhisperModel(model_size, device=settings.device, compute_type=settings.compute_type)

    # or run on GPU with INT8
    # model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
    # or run on CPU with INT8
    # model = WhisperModel(model_size, device="cpu", compute_type="int8")

    segments, info = model.transcribe("input.wav", beam_size=5)

    #print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

    for segment in segments:
        print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
    return segment.text

def Speech_to_Text_Parser():
    try:
        text = speech_to_text_processer()
        #print("Speech_to_text_processer_successfully")
    except Exception as e:
        print (e)
        raise RuntimeError("Exception in first playsound")
    return text 


#Teste die Funktion einzeln
#Speech_to_Text_Parser()