export interface IUserProfile {
    email: string;
    is_active: boolean;
    is_superuser: boolean;
    full_name: string;
    id: number;
    qr: string;
    is_teacher: boolean;
}

export interface IUserProfileUpdate {
    email?: string;
    full_name?: string;
    password?: string;
    is_active?: boolean;
    is_superuser?: boolean;
    is_teacher?: boolean;
    delete?: boolean;
}

export interface IUserProfileCreate {
    email: string;
    full_name?: string;
    password?: string;
    is_active?: boolean;
    is_superuser?: boolean;
    is_teacher?: boolean;
}

export interface ICreateSchool{
    school_name?: string;
}

export interface ISchoolProfile{
    school_name?: string;
    school_id?: number;
}

export interface ICreateProjet{
    project_name?: string;
    group_name?: string;
    description?: string;
    links?: string;
    vote_counter?: number;
    teacher_id?: number;
    school_id?: number;
}