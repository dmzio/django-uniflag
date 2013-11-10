function prepare_flag_form(url) {
    var reveal_btns = $("[id*='uniflag-reveal-btn-']");
    var modal_add_forms = $("[id*='uniflag-add-form-modal-']");
    var inline_add_forms = $("[id*='uniflag-add-form-inline-']");
    reveal_btns.show();

    modal_add_forms.dialog({
        autoOpen: false,
        modal: true,
        buttons: {
            Submit: function () {
                $(this).dialog("close");
                var part_id = partial_id($(this).attr('id'));
                $.post(url, modal_add_forms.filter("[id*='" + part_id + "']").children('form').serialize()).done(function (data) {
                    reveal_btns.filter("[id*='" + part_id + "']").hide();
                });
            },
            Cancel: function () {
                $(this).dialog("close");
            }
        }

    });

    reveal_btns.click(function () {
        var part_id = partial_id($(this).attr('id'));
        modal_add_forms.filter("[id*='" + part_id + "']").dialog('open');
    });

    inline_add_forms.find(':radio').change(function (e) {
        var form_el = $(this).parents('form');
        $.post(url, form_el.serialize()).done(function (data) {
            form_el.hide();
        });
    });


}

function partial_id(full_id) {
    var patt = /[-\d]+$/;
    return full_id.match(patt);
}

function enhance_flag_form(img_dir_url) {
    $(".uniflag-form").find('input:radio').each(function (index) {
        var inp_label = $("label[for='" + $(this).attr('id') + "']")
        if (inp_label.length == 0) {
            inp_label = $(this).closest('label')
        }
        var title = $(inp_label).html();
        var btn = $("<button class=\"btn uniflag-inp-btn\" id=\"btn-for-" + $(this).attr('id') + "\">" + title + "</button>").insertAfter(this);
        btn.attr('title', title);
        btn.addClass($(this).attr('class'));
        if ($(this).prop("checked")) {
            btn.addClass('active');
        }
        btn.data('uniflag-for-input', $(this).attr('id'));

        $(this).hide();
        inp_label.hide();

    });

    $('button.uniflag-inp-btn').click(function (e) {
        e.preventDefault();
        var radio_inp = $('#' + $(this).data('uniflag-for-input'));
        if (!radio_inp.prop("checked")) {
            radio_inp.attr("checked", true);
            $(this).parent('form').find('.uniflag-inp-btn').removeClass('active');
            $(this).addClass('active');
            radio_inp.change();
        }
        console.log();

    });

}