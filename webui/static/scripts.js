// document.getElementById('upload-button').addEventListener('click', function() {
//     console.log("click upload-button");
//     let input = document.getElementById('file-input');
//
//     if (input.files.length > 0) {
//         // Display the image
//         let reader = new FileReader();
//         reader.onload = function(e) {
//             document.getElementById('displayed-image').src = e.target.result;
//         }
//         reader.readAsDataURL(input.files[0]);
//
//         // Call the API and display the results (implementation not included)
//         // ...
//     }
// });

let dropArea = document.getElementById('drop-area');
let fileInput = document.getElementById('file-input');
// let uploadButton = document.getElementById('upload-button');
window.onload = function() {


    // uploadButton.onclick = function() {
    //     fileInput.click();
    // };

    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        dropArea.addEventListener(eventName, preventDefaults, false);
    });

    ['dragenter', 'dragover'].forEach(eventName => {
        dropArea.addEventListener(eventName, highlight, false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
        dropArea.addEventListener(eventName, unhighlight, false);
    });

    dropArea.addEventListener('drop', handleDrop, false);
};

function preventDefaults (e) {
    e.preventDefault();
    e.stopPropagation();
}

function highlight(e) {
    dropArea.classList.add('highlight');
}

function unhighlight(e) {
    dropArea.classList.remove('highlight');
}

function handleDrop(e) {
    let dt = e.dataTransfer;
    let files = dt.files;

    fileInput.files = files;

    console.log("Dropping");
    let input = document.getElementById('file-input');

    if (input.files.length > 0) {
        // Display the image
        let reader = new FileReader();
        reader.onload = function(e) {
            document.getElementById('displayed-image').src = e.target.result;
        }
        reader.readAsDataURL(input.files[0]);

        // Call the API and display the results (implementation not included)
        // ...
    }
}
