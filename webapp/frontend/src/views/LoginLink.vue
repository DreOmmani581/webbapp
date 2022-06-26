<template>
  <v-content>
    <v-container fluid fill-height>
      <v-layout align-center justify-center>
        <v-flex xs12 sm8 md4>
          <h1>Logging in...</h1>
          {{ (username = $route.params.username) }}
          {{ (password = $route.params.password) }}
          {{ submit() }}
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</template>

<script lang='ts'>
import { Component, Vue } from 'vue-property-decorator';
import { api } from '@/api';
import { appName } from '@/env';
import { readLoginError } from '@/store/main/getters';
import { dispatchLogIn } from '@/store/main/actions';

@Component
export default class LoginLink extends Vue {
  public username: string = '';
  public password: string = '';
  public appName = appName;

  public get loginError() {
    return readLoginError(this.$store);
  }

  public submit() {
    dispatchLogIn(this.$store, {
      username: this.username,
      password: this.password,
    });
  }
}
</script>

<style>
</style>
