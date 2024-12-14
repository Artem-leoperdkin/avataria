document.getElementById('registrationForm').addEventListener('submit', function(event) {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;
    const errorMessage = document.getElementById('errorMessage');

    errorMessage.textContent = "";

    if (password !== confirmPassword) {
        errorMessage.textContent = "Пароли не совпадают!";
        event.preventDefault(); 
        return false;
    } else if (!email || !password || !confirmPassword) {
        errorMessage.textContent = "Заполните все поля!";
        event.preventDefault(); 
        return false;
    }
});