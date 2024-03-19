<script>
        function uploadAudio() {
            const fileInput = document.getElementById('audioFile');
            const file = fileInput.files[0];
            const formData = new FormData();
            formData.append('audioFile', file);

            fetch('/api/process_audio', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                // Handle response as needed
            })
            .catch(error => console.error('Error:', error));
        }
 </script>