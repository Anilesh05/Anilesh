# Task 1

Question :-

   - Create a directory named "data" in HDFS.
   - Create an empty file named "sample.txt" inside the "data" directory.
   - List the contents of the "data" directory.
   - Upload a file named "localfile.txt" from your local filesystem to the "data" directory in HDFS.
   - Retrieve the "sample.txt" file from HDFS to your local filesystem.

commands :- 

            !hdfs dfs -mkdir data
            !hdfs dfs -touchz data/sample.txt
            !hdfs dfs -ls data
            !echo "Hello, this is a local file." > localfile.txt
            !hdfs dfs -put localfile.txt data/
            !hdfs dfs -get data/sample.txt


# Task 2

Question :-

   - Create a directory named "logs" in HDFS.
   - Copy a file named "server.log" from the local filesystem to the "logs" directory in HDFS.
   - Display the contents of the "server.log" file stored in HDFS.
   - Rename the "server.log" file to "app_logs.txt" in HDFS.
   - Remove the "app_logs.txt" file from HDFS.

commands :- 

            !hdfs dfs -mkdir logs
            !echo "This is a server log file." > server.log
            !hdfs dfs -put server.log logs/
            !hdfs dfs -cat logs/server.log
            !hdfs dfs -mv logs/server.log logs/app_logs.txt
            !hdfs dfs -rm logs/app_logs.txt


# Task 3

Question :-

   - Create a directory named "input" in HDFS.
   - Upload multiple local files (e.g., file1.txt, file2.txt) to the "input" directory in HDFS.
   - Check the existence of the uploaded files in the "input" directory.
   - Download all files from the "input" directory in HDFS to a local directory named "downloads".
   - Remove all files from the "input" directory in HDFS.

commands :- 
            
            !hdfs dfs -mkdir input
            !echo "Content of file1.txt" > file1.txt
            !echo "Content of file2.txt" > file2.txt
            !hdfs dfs -put file1.txt file2.txt input/
            !hdfs dfs -test -e input/file1.txt && echo "File exists"
            !hdfs dfs -test -e input/file2.txt && echo "File exists"
            !hdfs dfs -get input/* downloads/
            !hdfs dfs -rm input/*
            

# Task 4

Question :-

    - Create a directory named "documents" in HDFS.
    - Upload a local file named "report.docx" to the "documents" directory in HDFS.
    - List the contents of the "documents" directory to verify the upload.
    - Move the "report.docx" file to a new directory named "archived" within the "documents" directory.
    - Remove the "archived" directory from HDFS.

commands :- 

            !hdfs dfs -mkdir documents
            !echo "This is a report document." > report.docx
            !hdfs dfs -put report.docx documents/
            !hdfs dfs -ls documents
            !hdfs dfs -mv documents/report.docx documents/archived/
            !hdfs dfs -rmr documents/archived/


# Task 5

Question :-

    - Create a directory named "images" in HDFS.
    - Upload an image file named "photo.jpg" to the "images" directory.
    - Retrieve the "photo.jpg" file from HDFS to your local filesystem.
    - Create a duplicate copy of the "photo.jpg" file named "backup.jpg" in the "images" directory.
    - Display the contents of the "images" directory to verify the presence of both files.

commands :- 

            !hdfs dfs -mkdir images
            !echo "This is a sample image." > photo.jpg
            !hdfs dfs -put photo.jpg images/
            !hdfs dfs -get images/photo.jpg
            !hdfs dfs -cp images/photo.jpg images/backup.jpg
            !hdfs dfs -ls images/


# Task 6

Question :-

    - Create a directory named "videos" in HDFS.
    - Upload a video file named "movie.mp4" to the "videos" directory.
    - Move the "movie.mp4" file to a new directory named "archive" within the "videos" directory.
    - Rename the "archive" directory to "old_movies".
    - Delete the "old_movies" directory from HDFS.

commands :- 

            !hdfs dfs -mkdir videos
            !echo "This is a sample video." > movie.mp4
            !hdfs dfs -put movie.mp4 videos/
            !hdfs dfs -mv videos/movie.mp4 videos/archive/
            !hdfs dfs -mv videos/archive videos/old_movies
            !hdfs dfs -rmr videos/old_movies


# Task 7

Question :-

    - Create a directory named "temp" in HDFS.
    - Upload multiple local files (e.g., file1.txt, file2.txt, file3.txt) to the "temp" directory.
    - List all files in the "temp" directory along with their details.
    - Delete one of the uploaded files from the "temp" directory.
    - Display the remaining files in the "temp" directory.

commands :- 

            
            !hdfs dfs -mkdir temp
            !echo "Content of file1.txt" > file1.txt
            !echo "Content of file2.txt" > file2.txt
            !echo "Content of file3.txt" > file3.txt
            !hdfs dfs -put file1.txt file2.txt file3.txt temp/
            !hdfs dfs -ls -h temp/
            !hdfs dfs -rm temp/file1.txt
            !hdfs dfs -ls -h temp/
            

# Task 8

Question :-

    - Create a directory named "analytics" in HDFS.
    - Create an empty file named "data.txt" inside the "analytics" directory.
    - List the contents of the "analytics" directory to verify the creation of the file.
    - Upload a local file named "stats.csv" to the "analytics" directory in HDFS.
    - Retrieve the "stats.csv" file from HDFS to your local filesystem.

commands :- 

            
            !hdfs dfs -mkdir analytics
            !hdfs dfs -touchz analytics/data.txt
            !hdfs dfs -ls analytics/
            !echo "Column1,Column2,Column3" > stats.csv
            !hdfs dfs -put stats.csv analytics/
            !hdfs dfs -get analytics/stats.csv
            

# Task 9

Question :-

    - Create a directory named "logs" in HDFS.
    - Upload a log file named "server.log" to the "logs" directory.
    - Display the contents of the "server.log" file stored in HDFS.
    - Move the "server.log" file to a new directory named "archive" within the "logs" directory.
    - Remove the "archive" directory along with its contents.

commands :- 


            !hdfs dfs -mkdir logs
            !echo "This is a server log file." > server.log
            !hdfs dfs -put server.log logs/
            !hdfs dfs -cat logs/server.log
            !hdfs dfs -mv logs/server.log logs/archive/
            !hdfs dfs -rmr logs/archive/


# Task 10

Question :-

    - Upload a local file named "document.docx" to the root directory ("/") in HDFS.
    - Copy the "document.docx" file from HDFS to your local filesystem.
    - List the contents of the root directory ("/") in HDFS to verify the presence of the file.
    - Move the "document.docx" file to a new directory named "documents" in HDFS.
    - Delete the "documents" directory along with its contents.

commands :- 

            
            !echo "This is a sample document." > document.docx
            !hdfs dfs -put document.docx /
            !hdfs dfs -get /document.docx
            !hdfs dfs -ls /
            !hdfs dfs -mv /document.docx /documents
            !hdfs dfs -rmr /documents


# Task 11

Question :-

    - Create a directory named "output" in HDFS.
    - Upload a local file named "results.txt" to the "output" directory in HDFS.
    - Display the contents of the "results.txt" file stored in HDFS.
    - Rename the "results.txt" file to "final_results.txt" in HDFS.
    - Remove the "final_results.txt" file from HDFS.

commands :- 

            
            !hdfs dfs -mkdir output
            !echo "This is the result." > results.txt
            !hdfs dfs -put results.txt output/
            !hdfs dfs -cat output/results.txt
            !hdfs dfs -mv output/results.txt output/final_results.txt
            !hdfs dfs -rm output/final_results.txt
            

# Task 12

Question :-

    - Create a directory named "input_files" in HDFS.
    - Upload multiple local files (e.g., file1.txt, file2.txt) to the "input_files" directory in HDFS.
    - List all files in the "input_files" directory along with their details.
    - Copy one of the uploaded files to a new location within HDFS.
    - Delete all files from the "input_files" directory in HDFS.

commands :- 

            
            !hdfs dfs -mkdir input_files
            !echo "Content of file1.txt" > file1.txt
            !echo "Content of file2.txt" > file2.txt
            !hdfs dfs -put file1.txt file2.txt input_files/
            !hdfs dfs -ls -h input_files/
            !hdfs dfs -cp input_files/file1.txt input_files/copied_file.txt
            !hdfs dfs -rmr input_files/*


# Task 13

Question :-

    - Create a directory named "temp_files" in HDFS.
    - Upload a local file named "temp.txt" to the "temp_files" directory in HDFS.
    - Display the contents of the "temp.txt" file stored in HDFS.
    - Rename the "temp.txt" file to "new_temp.txt" in HDFS.
    - Remove the "new_temp.txt" file from HDFS.

commands :- 

            
            !hdfs dfs -mkdir temp_files
            !echo "This is a temp file." > temp.txt
            !hdfs dfs -put temp.txt temp_files/
            !hdfs dfs -cat temp_files/temp.txt
            !hdfs dfs -mv temp_files/temp.txt temp_files/new_temp.txt
            !hdfs dfs -rm temp_files/new_temp.txt
