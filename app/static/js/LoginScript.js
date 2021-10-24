/* function mostrarPassword() {
    var cambio = document.getElementById("txtPassword");
    if (cambio.type == "password") {
        cambio.type = "text";
        $('.icon').removeClass('fa fa-eye-slash').addClass('fa fa-eye');
    } else {
        cambio.type = "password";
        $('.icon').removeClass('fa fa-eye').addClass('fa fa-eye-slash');
    }
} */


const getTitleMessageFromCategory = category => {
    const titles = {
        'success': 'Bien hecho!',
        'warning': 'Atención!',
        'info': 'Atención!',
        'error': 'Oops...!',
    }
    return titles[category]
}

function showMessageAlert(category, message) {
    Swal.fire({
        icon: category,
        title: getTitleMessageFromCategory(category),
        text: message
    })
}