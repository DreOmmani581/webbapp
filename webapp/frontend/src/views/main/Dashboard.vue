<template>
  <v-container fluid>
    <v-card class='ma-3 pa-3'>
      <v-card-title primary-title>
        <div class='headline primary--text'>
        <img width='400' height='88' src='https://wirfuerschule.de/wp-content/uploads/2020/05/wirfu%CC%88rschule_logo-1024x226.png'>
        </div>
      </v-card-title>
      <v-card-text>
        <div class='headline font-weight-light ma-5'>Welcome {{greetedUser}}</div>
      </v-card-text>
      <v-card-actions>
        <v-btn to='/account/main/ProjectView'>Mein Projekt</v-btn>
        <v-btn to='/account/main/projectlist'>Alle Projekte</v-btn>
        <!--
        <v-btn to='/account/main/profile/password'>Change Password</v-btn>
        -->
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script lang='ts'>
import { Component, Vue } from 'vue-property-decorator';
import { Store } from 'vuex';
import { readUserProfile } from '@/store/main/getters';
@Component
export default class Dashboard extends Vue {
  get greetedUser() {
    const userProfile = readUserProfile(this.$store);
    if (userProfile) {
      if (userProfile.full_name) {
        return userProfile.full_name;
      } else {
        return userProfile.email;
      }
    }
  }
}
</script>

<style>
.v-toolbar__content{
      background-image: linear-gradient(160deg, #5AC6CE 0%, #28FFCF 73%);
}
</style>