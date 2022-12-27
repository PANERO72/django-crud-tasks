const indexPage = document.getElementById("index-page");
const tasksPage = document.getElementById("tasks-page");
const createTaskPage = document.getElementById("create-task-page");
const booksDetailsPage = document.getElementById("book-details-page");

const indexLink = document.getElementById("index-link");
const tasksLink = document.getElementById("tasks-link");
const createTaskLink = document.getElementById("create-task-link");
const logoutLink = document.getElementById("logout-link");
const loginLink = document.getElementById("login-link");
const adminLink = document.getElementById('admin-link');

const tasksListComplete = document.getElementById("tasks-list-complete");
const tasksListEmpty = document.getElementById("tasks-list-empty");

const btnsEliminar = document.querySelectorAll('a[data-task="delete"]');

// const editTaskForm = document.getElementById('edit-task-form');

const elementsLabels = document.querySelectorAll('label[for^="id_"]');
   elementsLabels.forEach(element => {
       element.classList.add("form-label");
   });

(function () {

    btnsEliminar.forEach((btn) => {
		btn.addEventListener("click", function(e){
			e.preventDefault();
			Swal.fire({
				title: '¿Está seguro?',
				text: '¿Desea eliminar esta tarea?',
				icon: 'warning',
				showCancelButton: true,
				confirmButtonColor: '#3085d6',
				cancelButtonColor: '#d33',
				confirmButtonText: 'Aceptar',
                cancelButtonText: 'Cancelar',
				backdrop: true,
				allowOutsideClick: false,
				allowEscapeKey: false,
			}).then((result) => {
				if (result.isConfirmed) {
					location.href = e.target.href;
				}
			});
		});
	});

	if (indexPage) {

		indexLink.style = "cursor: default; pointer-events: none;";
		indexLink.classList.add('active');
		indexLink.setAttribute('aria-current', 'page');

		if (tasksLink.classList.contains('active')) {
			tasksLink.classList().remove('active');
		}
		if (createTaskLink.classList.contains('active')) {
			createTaskLink.classList().remove('active');
		}
		if (logoutLink.classList.contains('active')) {
			logoutLink.classList().remove('active');
		}
		if(loginLink){
			if (loginLink.classList.contains('active')) {
				loginLink.classList().remove('active');
			}
		}if(adminLink.classList.contains('active')){
			adminLink.classList().remove('active');
		}

		tasksLink.removeAttribute('aria-current');
		createTaskLink.removeAttribute('aria-current');
		logoutLink.removeAttribute('aria-current');
		adminLink.removeAttribute('aria-current');

		if(loginLink){
			loginLink.removeAttribute('aria-current');
		}
			
	} else if (tasksPage) {		

		tasksLink.style = "cursor: default; pointer-events: none;";
		tasksLink.classList.add('active');
		tasksLink.setAttribute('aria-current', 'page');

		if (indexLink.classList.contains('active')) {
			indexLink.classList().remove('active');
		}
		if (createTaskLink.classList.contains('active')) {
			createTaskLink.classList().remove('active');
		}
		if (logoutLink.classList.contains('active')) {
			logoutLink.classList().remove('active');
		}
		if(adminLink.classList.contains('active')){
			adminLink.classList().remove('active');
		}
		if (loginLink) {
			
			if (loginLink.classList.contains('active')) {
				loginLink.classList().remove('active');
			}
		}

		indexLink.removeAttribute('aria-current');
		createTaskLink.removeAttribute('aria-current');
		logoutLink.removeAttribute('aria-current');
		adminLink.removeAttribute('aria-current');

		if(loginLink){

			loginLink.removeAttribute('aria-current');
		}

		if (tasksListComplete) {
			tasksPage.classList.add('hh-100');
		}
		else{
		 	tasksPage.classList.add('h-781');
		}

		// console.log(tasksListComplete.length);

	} else if(createTaskPage){

		createTaskLink.style = "cursor: default; pointer-events: none;";
		createTaskLink.classList.add('active')
		createTaskLink.setAttribute('aria-current', 'page');

		if (indexLink.classList.contains('active')) {
			indexLink.classList().remove('active');
		}
		if (tasksLink.classList.contains('active')) {
			tasksLink.classList().remove('active');
		}
		if (logoutLink.classList.contains('active')) {
			logoutLink.classList().remove('active');
		}
		if(adminLink.classList.contains('active')){
			adminLink.classList.remove('active');
		}
		if (loginLink) {
			
			if (loginLink.classList.contains('active')) {
				loginLink.classList().remove('active');
			}
		}

		indexLink.removeAttribute('aria-current');
		tasksLink.removeAttribute('aria-current');
		logoutLink.removeAttribute('aria-current');
		adminLink.removeAttribute('aria-current');
		
		if(loginLink){

			loginLink.removeAttribute('aria-current');
		}

	}

	// editTaskForm.children('label').classList.add('form-label');

})();