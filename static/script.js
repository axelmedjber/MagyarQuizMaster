document.addEventListener('DOMContentLoaded', function() {
    // Quiz logic
    const quizForm = document.getElementById('quiz-form');
    const questionContainers = document.querySelectorAll('.question-container');
    const nextButtons = document.querySelectorAll('.next-button');
    const prevButtons = document.querySelectorAll('.prev-button');
    const submitButton = document.getElementById('submit-button');
    const progressBar = document.getElementById('quiz-progress');
    const timerDisplay = document.getElementById('timer-display');
    
    // Initialize timer if element exists (bonus feature)
    let quizTimer;
    let timeLeft = 300; // 5 minutes in seconds
    
    if (timerDisplay) {
        startTimer();
    }
    
    // Start quiz timer
    function startTimer() {
        updateTimerDisplay();
        quizTimer = setInterval(function() {
            timeLeft--;
            updateTimerDisplay();
            
            if (timeLeft <= 0) {
                clearInterval(quizTimer);
                if (quizForm) {
                    quizForm.submit(); // Auto-submit when time is up
                }
            }
        }, 1000);
    }
    
    // Update timer display
    function updateTimerDisplay() {
        const minutes = Math.floor(timeLeft / 60);
        const seconds = timeLeft % 60;
        timerDisplay.textContent = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
        
        // Change color when less than 1 minute remains
        if (timeLeft < 60) {
            timerDisplay.classList.add('text-danger');
        }
    }
    
    // Show a specific question
    function showQuestion(index) {
        // Ensure valid index
        if (index < 0 || index >= questionContainers.length) {
            console.error("Invalid question index:", index);
            return;
        }
        
        // Hide all questions first
        questionContainers.forEach(container => {
            container.classList.add('hidden');
            container.classList.remove('fade-in');
        });
        
        // Show the current question
        questionContainers[index].classList.remove('hidden');
        questionContainers[index].classList.add('fade-in');
        
        // Update progress bar
        if (progressBar) {
            const progressPercentage = ((index + 1) / questionContainers.length) * 100;
            progressBar.style.width = `${progressPercentage}%`;
            progressBar.setAttribute('aria-valuenow', progressPercentage);
        }
        
        // Hide all navigation buttons first
        nextButtons.forEach(btn => btn.classList.add('hidden'));
        prevButtons.forEach(btn => btn.classList.add('hidden'));
        
        // Show appropriate navigation buttons for current question
        nextButtons.forEach(btn => {
            if (parseInt(btn.dataset.questionIndex) === index && 
                index < questionContainers.length - 1) {
                btn.classList.remove('hidden');
            }
        });
        
        prevButtons.forEach(btn => {
            if (parseInt(btn.dataset.questionIndex) === index && index > 0) {
                btn.classList.remove('hidden');
            }
        });
        
        // Show/hide submit button based on whether we're on the last question
        if (submitButton) {
            if (index === questionContainers.length - 1) {
                console.log("Showing submit button on last question");
                submitButton.classList.remove('hidden');
            } else {
                submitButton.classList.add('hidden');
            }
        }
        
        console.log(`Showing question ${index + 1}/${questionContainers.length}`);
    }
    
    // Initialize quiz if questions exist
    if (questionContainers.length > 0) {
        showQuestion(0);
        
        // Next button event listeners
        nextButtons.forEach(button => {
            button.addEventListener('click', function() {
                const currentIndex = parseInt(this.dataset.questionIndex);
                showQuestion(currentIndex + 1);
            });
        });
        
        // Previous button event listeners
        prevButtons.forEach(button => {
            button.addEventListener('click', function() {
                const currentIndex = parseInt(this.dataset.questionIndex);
                showQuestion(currentIndex - 1);
            });
        });
    }
    
    // Option selection enhancement
    const optionInputs = document.querySelectorAll('.option-input');
    optionInputs.forEach(input => {
        input.addEventListener('change', function() {
            // Find the parent question container
            const questionContainer = this.closest('.question-container');
            
            // Enable next button for this question if needed
            const nextBtn = questionContainer.querySelector('.next-button');
            if (nextBtn) {
                nextBtn.disabled = false;
            }
        });
    });
});
