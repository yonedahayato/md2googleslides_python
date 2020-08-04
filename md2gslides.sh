MD_FILE_NAME=$1
echo markdown file name : ${MD_FILE_NAME}

PPTX_FILE_NAME=${MD_FILE_NAME%.*}.pptx
echo power point file name : ${PPTX_FILE_NAME}

pandoc ${MD_FILE_NAME} -o ${PPTX_FILE_NAME}
python3 ./script/upload_to_drive.py ${PPTX_FILE_NAME}
