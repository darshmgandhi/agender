$(document).ready(function() {

    $(".names_label").hide();

    function clearInputsFolders() {
        $(".names_label").hide();
        $('.names_input').val(``);
    }

    function showInputs() {
        switch ($("input:radio:checked").val()) {
            case 'Button':
                $('.name').show();
                break;
            case 'Input':
                $('.name, .placeholder').show();
                break;
            case 'Radio':
                $('.value, .name').show();
                break;
            case 'Checkbox':
                $('.value, .name').show();
                break;
            case 'Image':
                $('.value, .name').show();
                break;
            default:
                $(".names_label").hide();
        }
    }

    $('.radio-check').click(function() {
        clearInputsFolders();
        showInputs();
    });

    let valueText, nameText, placeholderText, button, input, radio, checkbox, inputType, file;
    const buttonRemove = `<button class="remove button end">-</button>` + `<br class="end">`;

    function getInputsName() {
        function checkNameValue(className) {
            return ($(`.${className}_text`).val());
        }

        valueText = checkNameValue('value');
        nameText = checkNameValue('name');
        placeholderText = checkNameValue('placeholder');
    }

    function getInputTypeValue() {
        inputType = $("input:radio:checked").val();
    }

    function getInputForAdd() {
        getInputsName();

        button = `<button>${nameText}</button>` + buttonRemove;

        input = `<label>` +
            `${nameText} <input type="text" placeholder="${placeholderText}">` +
            buttonRemove;

        radio = `<label>` +
            `<input type="radio" name="${nameText}"> ${valueText}</label>` +
            buttonRemove;

        checkbox = `<label>` +
            `<input type="checkbox" name="${nameText}"> ${valueText}</label>` +
            buttonRemove;

        file = `<label>` +
            `${nameText} <input type="file" placeholder="${placeholderText} title="">` +
            buttonRemove;
    }

    function removeError() {
        $('.error').remove();
    }

    function error() {
        removeError();
        $('.names_input:invalid').after('<span class="error">Pease enter details</span>');
    };


    function addInput() {
        removeError();
        getInputsName();
        getInputTypeValue();

        let resultFolder = `#results`;

        switch (inputType) {
            case 'Button':
                nameText !== '' ? $(resultFolder).append(button) : error();
                break;
            case 'Input':
                nameText !== '' && placeholderText !== '' ? $(resultFolder).append(input) :
                    error();
                break;
            case 'Radio':
                nameText !== '' && valueText !== '' ? $(resultFolder).append(radio) :
                    error();
                break;
            case 'Checkbox':
                nameText !== '' && valueText !== '' ? $(resultFolder).append(checkbox) :
                    error();
                break;
            case 'Image':
                nameText !== '' && valueText !== '' ? $(resultFolder).append(file) :
                    error();
                break;
            default:
                alert('Please enter the details');
        }
    }

    $('.add').click(function() {
        getInputForAdd();
        addInput();
    });

    $('.generate').click(function() {
        $('.results').appendTo("result.html");
        $(document).find(" .end").remove();
        let resultCode = $(' .results').html();
        let resultForm = '<form class="form">' + resultCode + '<button class="submit" type="submit">Submit</button>' +
            '</form>';
        $('#html').val(resultForm);

    });

    $('.reset').click(function() {
        clearInputsFolders();
        $('.results').html(``);
        $('#html').val(``);
        $("input:radio").prop('checked', false);
        $('.error').remove();
    });

    $(document).on("click", ".remove", function() {
        $(this).prev().remove();
        $(this).next().remove();
        $(this).remove();
    });
});