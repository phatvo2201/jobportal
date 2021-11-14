$(document).ready(function() {
    $('#id_part_time')[0].addEventListener('change', (event) => {
        let sequelField = $('#id_first_name').parents('p');
        if (event.target.checked) {
            sequelField.show();
        } else {
            sequelField.hide();
        }
    })
});