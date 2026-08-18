const button = document.getElementById("research-btn");

const loading = document.getElementById("loading");

const reportContent =
    document.getElementById("report-content");

const sourcesList =
    document.getElementById("sources-list");

const loadingText =
    document.getElementById("loading-text");


button.addEventListener("click", async () => {

    const question =
        document.getElementById("question").value.trim();


    if(question === ""){

        alert("Please enter a question.");

        return;

    }


    loading.hidden = false;
    button.disabled = true;

    button.textContent = "Researching...";


    reportContent.innerHTML = "";

    sourcesList.innerHTML = "";


    try {

    loading.hidden = false;

    loadingText.textContent =
        "Researching your question...";

    button.disabled = true;

    button.textContent = "Researching...";

    reportContent.innerHTML = "";

    sourcesList.innerHTML = "";


    const response = await fetch("/research", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            question: question
        })

    });


    if (!response.ok) {
        throw new Error(`HTTP error: ${response.status}`);
    }


    const data = await response.json();


    reportContent.innerHTML =
        marked.parse(data.report);


    data.sources.forEach(source => {

        const li = document.createElement("li");

        const a = document.createElement("a");

        a.href = source.url;

        a.target = "_blank";

        a.rel = "noopener noreferrer";

        a.textContent = source.title;

        li.appendChild(a);

        sourcesList.appendChild(li);

    });

}
catch (error) {

    console.error(error);

    reportContent.innerHTML = `
        <p>
            Something went wrong while generating the report.
        </p>
    `;

}
finally {

    loading.hidden = true;

    button.disabled = false;

    button.textContent = "🔍 Research";

}});