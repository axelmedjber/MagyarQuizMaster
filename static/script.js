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
        questionContainers.forEach((container, i) => {
            if (i === index) {
                container.classList.remove('hidden');
                container.classList.add('fade-in');
            } else {
                container.classList.add('hidden');
                container.classList.remove('fade-in');
            }
        });
        
        // Update progress bar
        if (progressBar) {
            const progressPercentage = ((index + 1) / questionContainers.length) * 100;
            progressBar.style.width = `${progressPercentage}%`;
            progressBar.setAttribute('aria-valuenow', progressPercentage);
        }
        
        // Show/hide navigation buttons based on current question
        if (nextButtons.length > 0) {
            nextButtons.forEach(btn => {
                if (parseInt(btn.dataset.questionIndex) === index && 
                    index < questionContainers.length - 1) {
                    btn.classList.remove('hidden');
                } else {
                    btn.classList.add('hidden');
                }
            });
        }
        
        if (prevButtons.length > 0) {
            prevButtons.forEach(btn => {
                if (parseInt(btn.dataset.questionIndex) === index && index > 0) {
                    btn.classList.remove('hidden');
                } else {
                    btn.classList.add('hidden');
                }
            });
        }
        
        // Show submit button on last question
        if (submitButton) {
            if (index === questionContainers.length - 1) {
                submitButton.classList.remove('hidden');
            } else {
                submitButton.classList.add('hidden');
            }
        }
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
