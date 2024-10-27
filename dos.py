import requests
import threading
import time

# Configuration
TARGET_URL = ""# Enter the url here
THREAD_COUNT = 10000  # Number of threads to spawn
REQUESTS_PER_THREAD = 10000  # Number of requests per thread
DELAY_BETWEEN_REQUESTS = 0.05  # Delay between requests (in seconds)

def send_requests():
    """Send multiple requests to the target URL."""
    for _ in range(REQUESTS_PER_THREAD):
        try:
            response = requests.get(TARGET_URL)
            print(f"[INFO] Status: {response.status_code}, Length: {len(response.content)}")
            time.sleep(DELAY_BETWEEN_REQUESTS)
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Request failed: {e}")

def stress_test():
    """Launch multiple threads to send concurrent requests."""
    threads = []

    print(f"[INFO] Starting stress test on {TARGET_URL} with {THREAD_COUNT} threads...")

    # Create and start threads
    for _ in range(THREAD_COUNT):
        thread = threading.Thread(target=send_requests)
        thread.start()
        threads.append(thread)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("[INFO] Stress test completed.")

if __name__ == "__main__":
    stress_test()
