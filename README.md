# Multithreaded vs Single-threaded Merge Sort

This Python program compares merge sort performance using single-threading and multithreading with `threading.Thread`.  
Run the script with `1q.py` to see timing results.  
Random data is generated, sorted, and timed using both approaches.  
Due to Python's GIL, multithreading may not significantly improve performance.

How it works:  
Single-threaded Merge Sort:
Recursively divides the list.
Sorts the left and right halves one after the other.
Merges the sorted halves into a final sorted list.

Multi-threaded Merge Sort:
Recursively divides the list like the single-threaded version.
Spawns two threads to sort the left and right halves in parallel.
Waits for both threads to complete using join().
Merges the sorted halves.

Sample output:  
single-threaded Merge Sort Time: 0.0065 seconds  
multi-threaded Merge Sort Time: 2.5485 seconds


# Quick Sort: Single vs Multi-threaded

This Python script compares single-threaded and multi-threaded quicksort performance.
The multi-threaded version uses Python’s threading module to sort partitions in parallel.  
Run with python `2q.py`

How It Works:  
The pivot is chosen as the last element in the array.
The array is split into:
Elements less than the pivot.
The pivot itself.
Elements greater than the pivot.
In the multi-threaded version, the left and right partitions are sorted in separate threads to potentially speed up execution.  
Sample output:  
Single-threaded quicksort: 0.0044 seconds  
Multi-threaded quicksort: 1.1295 seconds  


# Concurrent File Downloader  

This Python script downloads web resources using single-threaded and multi-threaded (concurrent) approaches.
Run it with python `3q.py` after installing dependencies using pip install requests.
It saves files in the downloaded_content folder and compares performance of both methods.  

How It Works:  

Single-threaded mode: Downloads one resource at a time.  
Multi-threaded mode: Launches multiple threads to download resources in parallel, up to a specified limit using a Semaphore.  
Uses requests.get() with streaming to efficiently handle large downloads.  
Shows total download time and compares performance (efficiency gain).  
Sample output:  
Web Resource Acquisition Tool (Demonstration)

Resources to be acquired:
• https://www.nytimes.com
• https://www.ubuntu.com
• https://www.reddit.com
• https://www.linkedin.com
• https://www.adobe.com

 Beginning single-thread retrieval...
[+] Retrieved resource_1746205147.bin (219.7 KB) in 0.40 secs
[+] Retrieved resource_1746205148.bin (22.5 KB) in 1.43 secs
[+] Retrieved resource_1746205149.bin (0.0 KB) in 1.04 secs
[+] Retrieved resource_1746205150.bin (15.3 KB) in 0.46 secs
[+] Retrieved resource_1746205151.bin (0.0 KB) in 1.15 secs

 Single-thread complete: 5/5 resources in 4.50 secs

