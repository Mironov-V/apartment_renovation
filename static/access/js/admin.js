function open() {
    add_open.onclick = function() {
        return document.getElementById('add').style.display = "block";
    }

    // update_open.onclick = function() {
    //     return document.getElementById('update').style.display = "block";
    // }

    delete_open.onclick = function() {
        return document.getElementById('delete').style.display = "block";
    }
}

function close() {
    close_add.onclick = function() {
        return document.getElementById('add').style.display = "none";
    }

    // close_update.onclick = function() {
    //     return document.getElementById('update').style.display = "none";
    // }

    close_delete.onclick = function() {
        return document.getElementById('delete').style.display = "none";
    }
}


close();
open();