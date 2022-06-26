<template>
  <v-container fluid>
    <v-card class='ma-3 pa-3'>
      <v-card-title primary-title>
        <div class='headline primary--text'>
          <img
            width='400'
            height='88'
            src='https://wirfuerschule.de/wp-content/uploads/2020/05/wirfu%CC%88rschule_logo-1024x226.png'
          />
        </div>
      </v-card-title>
      <v-card-text>
        <div style='text-align: center'><h1>Projekt Editor</h1></div>
        <br /><br />
        <vue-editor
          ref='vEditor'
          id='editor'
          v-model='content'
          :editor-toolbar='customToolbar'
        />
      </v-card-text>
      <v-card-actions>
        <div class='center'>
          <v-btn @click='preview'>Vorschau</v-btn>
          <v-btn @click='upload'>Hochladen</v-btn>
        </div>

        <!--
        <v-btn to='/account/main/profile/password'>Change Password</v-btn>
        -->
      </v-card-actions>
    </v-card>
  </v-container>
</template>


<script>
import { VueEditor } from 'vue2-editor';

export default {
  components: { VueEditor },

  data: () => ({
    content: '',
    customToolbar: [
      ['bold', 'italic', 'underline'],
      [{ list: 'ordered' }, { list: 'bullet' }],
      ['image', 'code-block'],
      [
        { align: '' },
        { align: 'center' },
        { align: 'right' },
        { align: 'justify' },
      ],
      [{ color: [] }],
    ],
  }),
  methods: {
    preview() {
      console.log('preview');
      console.log(this.$refs.vEditor.quill.getContents());
    },
    upload() {
      console.log('uplaod');
    },
  },
};
</script>

<style>
.v-toolbar__content {
  background-image: linear-gradient(160deg, #5ac6ce 0%, #28ffcf 73%);
}
</style>
