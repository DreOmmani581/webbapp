import axios from 'axios';
import { apiUrl } from '@/env';
import { IUserProfile, IUserProfileUpdate, IUserProfileCreate, ICreateSchool, ICreateProjet, ISchoolProfile } from './interfaces';

function authHeaders(token: string) {
  return {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
}

export const api = {
  async logInGetToken(username: string, password: string) {
    const params = new URLSearchParams();
    params.append('username', username);
    params.append('password', password);

    return axios.post(`${apiUrl}/api/v1/login/access-token`, params);
  },
  async getMe(token: string) {
    return axios.get<IUserProfile>(`${apiUrl}/api/v1/users/me`, authHeaders(token));
  },
  async updateMe(token: string, data: IUserProfileUpdate) {
    return axios.put<IUserProfile>(`${apiUrl}/api/v1/users/me`, data, authHeaders(token));
  },
  async getUsers(token: string) {
    return axios.get<IUserProfile[]>(`${apiUrl}/api/v1/users/`, authHeaders(token));
  },
  async updateUser(token: string, userId: number, data: IUserProfileUpdate) {
    return axios.put(`${apiUrl}/api/v1/users/${userId}`, data, authHeaders(token));
  },
  async createUser(token: string, data: IUserProfileCreate) {
    return axios.post(`${apiUrl}/api/v1/users/`, data, authHeaders(token));
  },
  async deleteUser(token: string, userId: number, data: IUserProfileUpdate) {
    return axios.post(`${apiUrl}/api/v1/users/${userId}`, data, authHeaders(token));
  },
  async uploadFile(file: FormData, projectId: number) {
    return axios.post(`${apiUrl}/api/v1/projects/upload/${projectId}`, file, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
  },

  async getFileNames(projectId: number) {
    return axios.get(`${apiUrl}/api/v1/projects/upload/${projectId}`, {
      headers: {
        'Access-Control-Allow-Origin': '*',
      },
    });
  },

  async passwordRecovery(email: string) {
    return axios.post(`${apiUrl}/api/v1/password-recovery/${email}`);
  },
  async createSchool(token: string, data: ICreateSchool) {
    return axios.post(`${apiUrl}/api/v1/schools/`, data, authHeaders(token));
  },

  async getSchools(token: string) {
    return axios.get<ISchoolProfile[]>(`${apiUrl}/api/v1/schools/`, authHeaders(token));
  },

  async createProject(token: string, data: ICreateProjet) {
    return axios.post(`${apiUrl}/api/v1/projects/`, data, authHeaders(token));
  },
  async resetPassword(password: string, token: string) {
    return axios.post(`${apiUrl}/api/v1/reset-password/`, {
      new_password: password,
      token,
    });
  },
  //brauch ich das IUserProfile?
  async getProjectData(token: string) {
    return axios.get<IUserProfile[]>(`${apiUrl}/api/v1/projects/`, authHeaders(token));
  },



};
