import os
import time
import threading
import requests
from urllib import parse as url_parser

def retrieve_web_resource(resource_url, destination="downloaded_content"):
    try:
        os.makedirs(destination, exist_ok=True)
        
        parsed = url_parser.urlparse(resource_url)
        output_filename = os.path.basename(parsed.path)
        if not output_filename:
            output_filename = f"resource_{int(time.time())}.bin"
        
        complete_path = os.path.join(destination, output_filename)

        begin = time.perf_counter()
        server_response = requests.get(resource_url, stream=True)
        server_response.raise_for_status()

        content_size = int(server_response.headers.get('content-length', 0))

        with open(complete_path, 'wb') as output:
            for data_block in server_response.iter_content(8192):
                if data_block:
                    output.write(data_block)

        elapsed = time.perf_counter() - begin
        print(f"[+] Retrieved {output_filename} ({content_size/1024:.1f} KB) in {elapsed:.2f} secs")
        return True

    except Exception as err:
        print(f"[!] Error retrieving {resource_url}: {str(err)}")
        return False

def single_thread_fetch(url_collection, target_dir="downloaded_content"):
    print("\n Beginning single-thread retrieval...")
    timer_start = time.perf_counter()
    successful = 0

    for web_url in url_collection:
        if retrieve_web_resource(web_url, target_dir):
            successful += 1

    total_duration = time.perf_counter() - timer_start
    print(f"\n Single-thread complete: {successful}/{len(url_collection)} resources in {total_duration:.2f} secs")
    return total_duration

def concurrent_fetch(url_list, target_dir="downloaded_content", max_concurrent=5):
    print(f"\n Initializing concurrent retrieval ({max_concurrent} workers)...")
    timer_start = time.perf_counter()
    completion_counter = threading.Semaphore(max_concurrent)
    results = [0]
    workers = []

    def fetch_worker(url):
        with completion_counter:
            if retrieve_web_resource(url, target_dir):
                with threading.Lock():
                    results[0] += 1

    for current_url in url_list:
        worker = threading.Thread(target=fetch_worker, args=(current_url,))
        workers.append(worker)
        worker.start()

    for worker in workers:
        worker.join()

    total_duration = time.perf_counter() - timer_start
    print(f"\n Concurrent retrieval complete: {results[0]}/{len(url_list)} resources in {total_duration:.2f} secs")
    return total_duration

def run_demo():
    print(" Web Resource Acquisition Tool (Demonstration)")
    print("---------------------------------------------")

    test_resources = [
        "https://www.nytimes.com",
        "https://www.ubuntu.com",
        "https://www.reddit.com",
        "https://www.linkedin.com",
        "https://www.adobe.com"
    ]

    print("\n Resources to be acquired:")
    for res in test_resources:
        print(f"• {res}")

    storage_location = "downloaded_content"
    worker_count = 5

    single_thread_time = single_thread_fetch(test_resources, storage_location)
    multi_thread_time = concurrent_fetch(test_resources, storage_location, worker_count)

    efficiency = single_thread_time / multi_thread_time if multi_thread_time > 0 else 0
    print("\n Efficiency Comparison:")
    print(f"- Single-thread duration: {single_thread_time:.2f} seconds")
    print(f"- Multi-thread duration: {multi_thread_time:.2f} seconds")
    print(f"- Efficiency gain: {efficiency:.2f}x")

    print("\n Resource acquisition completed.")

if __name__ == "_main_":
    run_demo()