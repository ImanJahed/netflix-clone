        function showModal(element) {
            // Retrieve data attributes
            const title = element.getAttribute('data-title');
            const description = element.getAttribute('data-description');
            const releaseDate = element.getAttribute('data-release-date');
            const genre = element.getAttribute('data-genre');
            const length = element.getAttribute('data-length');
            const imageCardUrl = element.getAttribute('data-image-card-url');
            const imageCoverUrl = element.getAttribute('data-image-cover-url');
            const dataVideoUrl = element.getAttribute('data-video-url');

            // Update the modal's content with the movie details
            const modal = document.getElementById('movieModal');
            modal.querySelector('.modal-content h2').textContent = title;
            modal.querySelector('.modal-content img').src = imageCoverUrl;
            modal.querySelector('.modal-content a').href = dataVideoUrl;
            modal.querySelector('.modal-content img').alt = title + " Cover Image";
            modal.querySelector('.modal-content .flex span:first-child').textContent = "Year: " + releaseDate;
            modal.querySelector('.modal-content .flex span:nth-child(2)').textContent = "Genre: " + genre;
            modal.querySelector('.modal-content .flex span:last-child').textContent = "Length: " + length ;
            modal.querySelector('.modal-content p').textContent = description;

            // Show the modal
            modal.style.display = 'block';
            setTimeout(() => {
                modal.classList.add('modal-show');
            }, 50);
        }

        function hideModal() {
            const modal = document.querySelector('.modal');
            modal.classList.remove('modal-show');
            setTimeout(() => {
                modal.style.display = 'none';
            }, 300);
        }


        window.onclick = function(event) {
            if (event.target === document.getElementById('movieModal')) {
                hideModal();
            }
        }

        function addItemToList() {
            const modal = document.getElementById('movieModal')
            var movieID = modal.querySelector('.modal-content a').href;

            $.ajax({
                url: "{% url 'add-to-list' %}",
                type: "POST",
                data: {
                    movie_id: movieID,
                    csrfmiddlewaretoken: "{{ csrf_token }}"
                },
                success: function(data) {
                    $('#addToListButton').text(data.message);

                    $('#addToListButton').prop('disabled', true);

                    console.log("Item added to list!");
                },
                error: function(xhr, errmsg, err) {

                    console.error("Error adding item to list: " + errmsg);
                }
            });
        }