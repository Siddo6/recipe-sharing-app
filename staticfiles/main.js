document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('back').addEventListener('click', function() {
        window.history.back();
    });
});

document.addEventListener('DOMContentLoaded', function() {
    var commentForm = document.getElementById('commentForm');
    
    if (commentForm) {
        commentForm.addEventListener('submit', function(event) {
            if (!window.confirm("Do you want to publish this comment?")) {
                // User clicked "Cancel" or closed the dialog, prevent the form submission
                event.preventDefault();
                console.log("User canceled the comment submission");
            }
        });
    }
});