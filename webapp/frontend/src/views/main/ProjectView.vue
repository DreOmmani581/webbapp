<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <div>
        <h3>
          <div id="groupName">{{ "Gruppe X" }}</div>
        </h3>
        <h1>
          <div id="titleProject">{{ "Some Project Title" }}</div>
        </h1>
      </div>
      <br /><br /><br />
      <div class="container">
        <!-- this is how showing pdf would look like src='http://localhost/api/v1/projects/upload/15/Motivationsschreiben.pdf' -->
        <embed
          id="pdfEmbed"
          src="/img/beispiel.pdf"
          width="100%"
          height="1000px  %"
          type="application/pdf"
        />
      </div>
      <br /><br />
      <div class="center">
        <h3>PDF Hochladen</h3>
        <input id="input" accept=".pdf" type="file" @change="onPdf" /><v-btn
          @click="clicked"
          >Hochladen</v-btn
        >
      </div>
    </v-card>
  </v-container>
</template>


<script src='https://unpkg.com/vue-pdf-embed'></script>
<script src='https://cdn.jsdelivr.net/npm/pdfjs-dist@2.14.305/build/pdf.min.js'></script>
<script lang='ts'>
import { Component, Vue } from "vue-property-decorator";
import { api } from "@/api";
import { dispatchGetProjectData } from "@/store/admin/actions";

function getData() {
  console.log("instant");
}

// <img id='examplePic' class='center' src='/img\icons/example.png'>

@Component
export default class ProjectView extends Vue {
  /**
   * eventlistener upload button
   */
  public clicked() {
    // get current file from input
    const inputField = document.getElementById("input") as HTMLInputElement;

    if (inputField != null) {
      // @ts-ignore: Object is possibly 'null'.
      const currentFile = inputField.files[0];
      // console.log(currentFile);
      const formData = new FormData();
      formData.append("files", currentFile);
      const projectId = 15; // for manual testing only !!!
      let response = api.uploadFile(formData, projectId);
      console.log(response);

      response = api.getFileNames(projectId);
      console.log(response);
      alert('PDF "" + currentFile.name + "" wurde hochgeladen');
    }
  }

  public async mounted() {
    getData();
    await dispatchGetProjectData(this.$store);
  }
}
</script>

<style>
#groupName {
  text-align: right;
}
#titleProject {
  text-align: center;
}
#div1 {
  width: auto;
  height: 85px;
  padding: 10px;
  border: 1px solid #aaaaaa;
  box-shadow: 3px 1px 1px black;
}
.v-toolbar__content {
  background-image: linear-gradient(160deg, #5ac6ce 0%, #28ffcf 73%);
}

.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
}
</style>