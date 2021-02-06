function menu_manager() {
    menu.onclick = function() {
        return document.getElementsByClassName("mobile_menu")[0].style.display = "block";
    }
    close_menu.onclick = function() {
        return document.getElementsByClassName("mobile_menu")[0].style.display = "none";
    }
}

menu_manager();

function modal_window_open(content = null) {
    document.getElementsByClassName("global_block")[0].style.display = "block";
    if (content == "query_tel") {
        return document.getElementsByClassName("win1")[0].style.display = "block";
    }
}

function modal_window_close(content_next = null) {
    document.getElementsByClassName("global_block")[0].style.display = "none";
    if (content_next == "query_tel") {
        return document.getElementsByClassName("win1")[0].style.display = "none";
    }
}


query_tel[0].onclick = function() {
    modal_window_open(content = "query_tel");
}
query_tel[1].onclick = function() {
    modal_window_open(content = "query_tel");
}
query_tel[2].onclick = function() {
    modal_window_open(content = "query_tel");
}
query_tel[3].onclick = function() {
    modal_window_open(content = "query_tel");
}
query_tel[4].onclick = function() {
    modal_window_open(content = "query_tel");
}
query_tel[5].onclick = function() {
    modal_window_open(content = "query_tel");
}
query_tel[6].onclick = function() {
    modal_window_open(content = "query_tel");
}
query_tel[7].onclick = function() {
    modal_window_open(content = "query_tel");
}
query_tel[8].onclick = function() {
    modal_window_open(content = "query_tel");
}
query_tel[9].onclick = function() {
    modal_window_open(content = "query_tel");
}


query_tel_close.onclick = function() {
    modal_window_close(content_next = "query_tel");
}