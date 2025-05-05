let data;
async function getJobPost() {
    url = "http://localhost:5000/filter_job/"
    try {
	const response = await fetch(url);
    if (!response.ok) {
	throw new Error(`response status: ${response.status}`)
    }
    const json = await response.json();
    console.log(json);
    data = json; 
    } catch (error) {
    console.error(error.message);
    }
}; 

const worktype_field = document.querySelector("#worktype")
const department_field = document.querySelector("#department")

const jobList = document.querySelector("#jobPostList")


function createJobDiv(title="Title",department="Department", worktype="Worktype",content="Content") {
    let div = document.createElement("div");
    let title_div = document.createElement("div");
    let department_div = document.createElement("div");
    let worktype_div = document.createElement("div");
    let content_div = document.createElement("div");
    title_div.textContent = title;
    department_div.textContent = department;
    worktype_div.textContent = worktype;
    content_div.textContent = content;
    div.appendChild(title_div);
    div.appendChild(department_div);
    div.appendChild(worktype_div);
    div.appendChild(content_div);
    div.classList.add("jobPostContainer")
    let children = div.children;
    for (let child of children) {
	child.classList.add("jobPost")}
    return div;
};

let query = () => {
    while (jobList.hasChildNodes()){
	jobList.removeChild(jobList.firstChild)}; 
    let worktype = worktype_field.value;
    let department = department_field.value;
    jobList.appendChild(createJobDiv());
    for (let i=0; i<data.length; i++){
	let jobpost = data[i];
	if (jobpost.worktype === worktype && jobpost.department === department) {
	jobList.appendChild(createJobDiv(jobpost.title, jobpost.department, jobpost.worktype, jobpost.content));
	} 
	
    }
}

const button = document.querySelector("button");

button.addEventListener("click", getJobPost())





