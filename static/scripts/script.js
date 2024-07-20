function ShowModal(e){
	isi = e.getAttribute('nilai-id');
	let getId ='modal'+isi
	let modal = document.getElementById(getId)
	console.log(modal)
	if(modal.style.display === 'block'){
		modal.style.display = 'none'
	}else{
		modal.style.display = 'block'
	}
}
