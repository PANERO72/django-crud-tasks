// const editTaskForm = document.getElementById('edit-task-form');

const elementsLabels = document.querySelectorAll('label[for^="id_"]');
const elementsInputsText = document.querySelectorAll('input[type=text]');
const elementsInputsPassword = document.querySelectorAll('input[type=password]');

elementsInputsText.forEach(element => {
	element.classList.add('form-control');
});

elementsLabels.forEach(element => {
    element.classList.add("form-label");
});

elementsInputsPassword.forEach(element => {
	element.classList.add('form-control');
});


(function () {

	

	// editTaskForm.children('label').classList.add('form-label');

})();