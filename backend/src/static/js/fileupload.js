function uploadFile() {

    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    if(file == null){
        const error = document.getElementById('file_input_invalid');
        error.classList.remove('hidden');
    }
    else{
    const formData = new FormData();
    formData.append('file', file);

    fetch('/fileupload/', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (response.status == 500) {
            const error = document.getElementById('file_input_wrong');
            error.classList.remove('hidden');;
        }
        else if(!response.ok){
            const error = document.getElementById('file_input_folder');
            error.classList.remove('hidden');
        }
        
    })
    .then(data => {
        console.log('File uploaded successfully:', data);
    })
    .catch(error => {
        console.error('There was an error uploading the file:', error);
        
        
    });
    }
}
