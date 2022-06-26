<template>
  <v-container fluid>
    <v-card class='ma-3 pa-3'>
      <v-card-title primary-title>
        <div class='headline primary--text'>Create User</div>
      </v-card-title>
      <v-card-text>
        <template>
          <v-form v-model='valid' ref='form' lazy-validation>
            <v-text-field
              label='Full Name'
              v-model='fullName'
              required
            ></v-text-field>
            <v-text-field
              label='E-mail'
              type='email'
              v-model='email'
              v-validate="'required|email'"
              data-vv-name='email'
              :error-messages="errors.collect('email')"
              required
            ></v-text-field>
            <div class='subheading secondary--text text--lighten-2'>
              User is superuser
              <span v-if='isSuperuser'>(currently is a superuser)</span
              ><span v-else>(currently is not a superuser)</span>
            </div>
            <v-checkbox label='Is Superuser' v-model='isSuperuser'></v-checkbox>
            <div class='subheading secondary--text text--lighten-2'>
              User is teacher
              <span v-if='isTeacher'>(currently is a teacher)</span
              ><span v-else>(currently is not a teacher)</span>
            </div>
            <v-checkbox label='Is Teacher' v-model='isTeacher'></v-checkbox>
            <div class='subheading secondary--text text--lighten-2'>
              User is active <span v-if='isActive'>(currently active)</span
              ><span v-else>(currently not active)</span>
            </div>
            <v-checkbox label='Is Active' v-model='isActive'></v-checkbox>
            <v-layout align-center>
              <v-flex>
                <v-text-field
                  type='password'
                  ref='password'
                  label='Set Password'
                  data-vv-name='password'
                  data-vv-delay='100'
                  v-validate='{ required: true }'
                  v-model='password1'
                  :error-messages="errors.first('password')"
                >
                </v-text-field>
                <v-text-field
                  type='password'
                  label='Confirm Password'
                  data-vv-name='password_confirmation'
                  data-vv-delay='100'
                  data-vv-as='password'
                  v-validate="{ required: true, confirmed: 'password' }"
                  v-model='password2'
                  :error-messages="errors.first('password_confirmation')"
                >
                </v-text-field>
              </v-flex>
            </v-layout>
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
    <v-card class='ma-3 pa-3'>
      <v-card-title primary-title>
        <div class='headline primary--text'>Generate user</div>
      </v-card-title>
      <v-card-text>
        <template>
          <v-form v-model='valid' ref='form' lazy-validation>
            <div class='subheading secondary--text text--lighten-2'>
              User is superuser
              <span v-if='isSuperuser'>(currently is a superuser)</span
              ><span v-else>(currently is not a superuser)</span>
            </div>
            <v-checkbox label='Is Superuser' v-model='isSuperuser'></v-checkbox>
            <div class='subheading secondary--text text--lighten-2'>
              User is teacher
              <span v-if='isTeacher'>(currently is a teacher)</span
              ><span v-else>(currently is not a teacher)</span>
            </div>
            <v-checkbox label='Is Teacher' v-model='isTeacher'></v-checkbox>
            <div class='subheading secondary--text text--lighten-2'>
              User is active <span v-if='isActive'>(currently active)</span
              ><span v-else>(currently not active)</span>
            </div>
            <v-checkbox label='Is Active' v-model='isActive'></v-checkbox>
          </v-form>
        </template>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn @click='generate'>Generate</v-btn>
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
} from '@/interfaces';
import { dispatchGetUsers, dispatchCreateUser } from '@/store/admin/actions';

@Component
export default class CreateUser extends Vue {
  public valid = false;
  public fullName: string = '';
  public email: string = '';
  public isActive: boolean = true;
  public isSuperuser: boolean = false;
  public setPassword = false;
  public password1: string = '';
  public password2: string = '';
  public isTeacher: boolean = false;

  public async mounted() {
    await dispatchGetUsers(this.$store);
    this.reset();
  }

  public reset() {
    this.password1 = '';
    this.password2 = '';
    this.fullName = '';
    this.email = '';
    this.isActive = true;
    this.isSuperuser = false;
    this.isTeacher = false;
    this.$validator.reset();
  }

  public cancel() {
    this.$router.back();
  }

  public async generate() {
    const updatedProfile: IUserProfileCreate = {
      email: 'generate@generated.com',
    };
    if (this.fullName) {
      updatedProfile.full_name = 'generate';
    }
    if (this.email) {
      updatedProfile.email = 'generate@generated.com';
    }
    updatedProfile.is_active = this.isActive;
    updatedProfile.is_superuser = this.isSuperuser;
    updatedProfile.password = 'generate';
    updatedProfile.is_teacher = this.isTeacher;
    await dispatchCreateUser(this.$store, updatedProfile);
    this.$router.push('/account/main/admin/users');
  }

  public async submit() {
    if (await this.$validator.validateAll()) {
      const updatedProfile: IUserProfileCreate = {
        email: this.email,
      };
      if (this.fullName) {
        updatedProfile.full_name = this.fullName;
      }
      if (this.email) {
        updatedProfile.email = this.email;
      }
      updatedProfile.is_active = this.isActive;
      updatedProfile.is_superuser = this.isSuperuser;
      updatedProfile.password = this.password1;
      updatedProfile.is_teacher = this.isTeacher;
      await dispatchCreateUser(this.$store, updatedProfile);
      this.$router.push('/account/main/admin/users');
    }
  }
}
</script>
