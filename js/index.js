
document.addEventListener('DOMContentLoaded', function () {

    document.getElementById('login-button').addEventListener('click', function () {

        var username = document.getElementById('username').value;
        var password = document.getElementById('password').value;

        // Aquí debes realizar tu lógica de validación
        // Por ejemplo, podrías comprobar si ambos campos están llenos
        if (username.trim() === '' || password.trim() === '') {
            alert('Por favor, completa todos los campos.');
        } else {

            alert('Datos válidos. ¡Inicio de sesión exitoso!');
        }
    });


    document.getElementById('cancel-button').addEventListener('click', function () {
        alert('Inicio de sesión cancelado.');
    });
});
