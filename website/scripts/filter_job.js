let data;
async function getJobPost() {
    try {
	let url = "http://localhost:5000/filter_job/";
	const response = await fetch(url);
	if (!response.ok) {
	    throw new Error(`response status: ${response.status}`);
	};
    const json = await response.json();
    console.log(json);
    data = json; 
    } catch (error) {
    console.error(error.message);
    }
}
getJobPost();

const worktype_field = document.querySelector("#worktype");
const department_field = document.querySelector("#department");
const salary_field = document.querySelector("#salary");

const jobList = document.querySelector("#jobPostList");
jobList.textContent = "Waiting";

(function jobPostStateControl(){
    timer = setInterval(()=>{
	if (data){
	    clearInterval(timer)
	    jobList.textContent="Fetched data";
	} else {
	    console.log("nodata")
	    switch (jobList.textContent) {
		case "Waiting":
		console.log("waiting");
		getJobPost();
		jobList.textContent = "Waiting.";
		break;
		case "Waiting.":
		getJobPost();
		jobList.textContent = "Waiting.."
		break;
		case "Waiting..":
		getJobPost();
		jobList.textContent = "Waiting..."
		break;
		case "Waiting...":
		getJobPost();
		jobList.textContent = "Waiting"
	    }
	}
    }, 500)
}) (); 


function createJobCard(title, address, salary, worktype, department, content){
    let card = document.createElement("div");
    let title_ele = document.createElement("h2");
    let address_ele = document.createElement("h3");
    let list = document.createElement("ul");
    let salary_ele = document.createElement("li");
    let worktype_ele = document.createElement("li");
    let department_ele = document.createElement("li");
    title_ele.textContent = title;
    address_ele.textContent = address;
    salary_ele.textContent = salary;
    worktype_ele.textContent = worktype;
    department_ele.textContent = department;
    list.appendChild(salary_ele);
    list.appendChild(worktype_ele);
    list.appendChild(department_ele);
    card.appendChild(title_ele);
    card.appendChild(address_ele);
    card.appendChild(list);
    return card;
}

/**
function createJobDiv(title="Title",department="Department", worktype="Worktype",content="Content", salary="Salary") {
    let div = document.createElement("div");
    let title_div = document.createElement("div");
    let department_div = document.createElement("div");
    let worktype_div = document.createElement("div");
    let content_div = document.createElement("div");
    let salary_div = document.createElement("div")
    title_div.textContent = title;
    department_div.textContent = department;
    worktype_div.textContent = worktype;
    content_div.textContent = content;
    salary_div.textContent = salary;
    div.appendChild(title_div);
    div.appendChild(department_div);
    div.appendChild(worktype_div);
    div.appendChild(content_div);
    div.appendChild(salary_div);
    div.classList.add("jobPostContainer")
    div.addEventListener("click", ()=>{form.style.display="flex";})
    let children = div.children;
    for (let child of children) {
	child.classList.add("jobPost")
    };
    return div;
};
**/

let query = () => {
    while (jobList.hasChildNodes()){
	jobList.removeChild(jobList.firstChild)
    };
    let worktype = worktype_field.value;
    let department = department_field.value;
    let salary = salary_field.value;
    filtered_data = data.filter(jobpost => {
	jobpost.worktype == worktype;
	jobpost.department == department;
	parseInt(jobpost.salary.slice(0,-1)) >= parseInt(salary);
	
    })
    console.log(filtered_data);
    for (let i=0; i<filtered_data.length;i++){
	let jobpost = filtered_data[i];
	jobList.appendChild(createJobCard(jobpost.title, jobpost.address, jobpost.salary, jobpost.worktype, jobpost.department, jobpost.content));
    }
}

/** let query = () => {
    while (jobList.hasChildNodes()){
	jobList.removeChild(jobList.firstChild)}; 
    let worktype = worktype_field.value;
    let department = department_field.value;
    jobList.appendChild(createJobDiv());
    if (worktype==="All" || department==="All"){
	if (worktype==="All" && department==="All"){
	    for (let i=0; i<data.length; i++){
		let jobpost = data[i];
		jobList.appendChild(createJobDiv(jobpost.title, jobpost.department, jobpost.worktype, jobpost.content, jobpost.salary));	
	    } 
	}else if (worktype==="All"){
	    for (let i=0; i<data.length; i++){
		let jobpost = data[i];
		if (jobpost.department === department) {
		jobList.appendChild(createJobDiv(jobpost.title, jobpost.department, jobpost.worktype, jobpost.content, jobpost.salary));
		};
	    };
	} else { 
	    for (let i=0; i<data.length; i++){
		let jobpost = data[i];
		if (jobpost.worktype === worktype) {
		jobList.appendChild(createJobDiv(jobpost.title, jobpost.department, jobpost.worktype, jobpost.content, jobpost.salary));
		};
	    };
	}
    } else {
	for (let i=0; i<data.length; i++){
	    let jobpost = data[i];
	    if (jobpost.worktype === worktype && jobpost.department === department) {
	    jobList.appendChild(createJobDiv(jobpost.title, jobpost.department, jobpost.worktype, jobpost.content, jobpost.salary));
	    };
	};
    };
};
**/
form.style.display="none";

async function postData(){
    let formData = new FormData(form)
    let url = "http://localhost:5000/upload"
    const response = await fetch(url, {
	    method: "POST",
	    body: formData 
    })
    
    const response2 = response.clone()
    try {
	json1 = await response.json()
	console.log(json1)
	submitStatus.textContent=JSON.stringify(json1.error,null);
    } catch(e) {
	const json2 = await response2.json()
	console.log(json2)
	submitStatus.textContent=json2
	console.error(e)
    }
}


const handleSubmit = (e) => {
    let formData = new FormData(form)
    let url = "http://localhost:5000/upload"
    e.preventDefault();
    form.style.display="none";
    postData();
}

form.addEventListener("submit", handleSubmit)
