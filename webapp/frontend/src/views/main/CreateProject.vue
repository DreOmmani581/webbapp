<template>
  <v-container fluid>
    <v-card class='ma-3 pa-3'>
      <v-card-title primary-title>
        <div class='headline primary--text'>Projekt Erstellen</div>
      </v-card-title>
      <v-card-text>
        <template>
          <v-form v-model='valid' ref='form' lazy-validation>
            <v-text-field
              label='Projektname'
              v-model='projectName'
              required
            ></v-text-field>
            <v-text-field
              label='Gruppenname'
              v-model='groupName'
              required
            ></v-text-field>
            <v-text-field
              label='Beschreibung'
              v-model='description'
              required
            ></v-text-field>
            <v-text-field
              label='Links'  
              v-model='links'
            ></v-text-field>
            
            
          </v-form>
        </template>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn @click='cancel'>Cancel</v-btn>
        <v-btn @click='reset'>Reset</v-btn>
        <v-btn @click='submit' :disabled='!valid'> Save </v-btn>
      </v-card-actions>
    </v-card>
    
  </v-container>
</template>

<script lang='ts'>
import { Component, Vue } from 'vue-property-decorator';
import {
  IUserProfile,
  IUserProfileUpdate,
  IUserProfileCreate,
  ICreateProjet,
} from '@/interfaces';
import { dispatchGetUsers, dispatchCreateUser, dispatchCreateProject } from '@/store/admin/actions';

@Component
export default class CreateProject extends Vue {
  public valid = false;
  public projectName: string = '';
  public groupName: string = '';
  public description: string = '';
  public links: string = '';

// IDs von schule und teacher sind grad noch hardcoded, müssen geholt werden
  public votes: number= 0;
  public teacherID=1;
  public schoolID=1;
  
  public async mounted() {
    await dispatchGetUsers(this.$store);
    this.reset();
  }

  public reset() {
    this.projectName = '';
    this.groupName = '';
    this.description = '';
    this.links = '';

    this.votes = 0;
    this.teacherID = 1;
    this.schoolID = 1;
    this.$validator.reset();
  }

  public cancel() {
    this.$router.back();
  }

 

  public async submit() {
    if (await this.$validator.validateAll()) {
      const newProject: ICreateProjet = {
       project_name: this.projectName,
        group_name: this.groupName,
        description: this.description,
        links: this.links,
        vote_counter: this.votes,
        teacher_id: this.teacherID,
        school_id: this.schoolID
      };
     
    
      await dispatchCreateProject(this.$store, newProject);
      this.$router.push('/account/main/admin/users');
    }
  }
}
</script>
