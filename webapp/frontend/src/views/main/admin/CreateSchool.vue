<template>
  <v-container fluid>
    <v-card class='ma-3 pa-3'>
      <v-card-title primary-title>
        <div class='headline primary--text'>Create School</div>
      </v-card-title>
      <v-card-text>
        <template>
          <v-form v-model='valid' ref='form' lazy-validation>
            <v-text-field
              label='Schoolname'
              v-model='fullName'
              required
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
  ICreateSchool,
} from '@/interfaces';
import { dispatchGetUsers, dispatchCreateUser, dispatchCreateSchool } from '@/store/admin/actions';
import { api } from '@/api';

@Component
export default class CreateUser extends Vue {
  public valid = false;
  public fullName: string = '';
 

  public async mounted() {
    await dispatchGetUsers(this.$store);
    this.reset();
  }

  public reset() {
    this.fullName = '';
    this.$validator.reset();
  }

  public cancel() {
    this.$router.back();
  }

  
  public async submit() {
    if (await this.$validator.validateAll()) {
      const school: ICreateSchool = {
        school_name: this.fullName,
      };
     
     
       await dispatchCreateSchool(this.$store, school);
      this.$router.push('/account/main/admin/users');
    }
  }
}
</script>
