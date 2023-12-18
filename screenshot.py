from PIL import ImageGrab
import time
INTERVAL_MINUTES = 5

def screenshot():
    timestamp = time.strftime("%Y%m%d%H%M%S")
    filename = f"screenshot_{timestamp}.png"
    print(f"Tirando screenshot: {filename}")
    screenshot = ImageGrab.grab()
    screenshot.save(filename)

if __name__ == "__main__":
    try:
        while True:
            screenshot()
            time.sleep(60 * INTERVAL_MINUTES)
    except KeyboardInterrupt:
        print("Script interrompido pelo usuário.")
