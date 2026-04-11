<script setup>
    import { useRouter } from 'vue-router'
    const router = useRouter()
    import { ref } from 'vue';


     const email = ref('');
     const password = ref('');
     const name = ref ('');
     const qualification = ref ('');
     const specialization = ref('');
     const experience_year = ref ('');


    const passwordError = ref('')

    const validatePassword = () => {
    if (password.value.length < 8 || !/[A-Z]/.test(password.value) ||!/[a-z]/.test(password.value) ||!/[0-9]/.test(password.value) ||!/[!@#$]/.test(password.value)){
        passwordError.value ='Your password length must be of 8 char long and contain atleast a uppercase,lowercase,numbers and special char'
        return false
    }
    else{
        passwordError.value = ''
        return true
    } 
    }
 

    async function validate(){
        if (!validatePassword()){
            alert("Please review your Password")
            return
        }
        if (email.value == "" || password.value == ""){
            alert("Email and Password should not be empty")
            return
        }
        if (name.value == "" || specialization.value == "" || experience_year.value ==""){
            alert("Please fill all * field")
            return
        }
        const user = {
            email : email.value,
            password : password.value,
            role: 'doctor',
            name:name.value,
            qualification:qualification.value,
            specialization:specialization.value,
            experience_years: experience_year.value
        }

        const response = await fetch('http://127.0.0.1:5000/api/register',{
            method: 'POST',
            headers:{
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(user)
        });
        console.log(response)

        if (!response.ok){
            const errordata= await response.json()
            console.log(errordata)
            alert(`Submission failed:${errordata.message}`)
            return
        }
    alert("Successfully register")
    router.push('/admin')

    }
    function Back(){
        router.push('/admin')
    }
</script>

<template>
     <div class="container-fluid">
        <div class = "row justify-content-center mt-3">
            <div class = "col-6 align-items-center">
                <h1 class = text-center>Doctor Registration</h1>
                <form @submit.prevent = "validate">
                    <div class="mb-3">
                        <label for="exampleInputEmail1" class="form-label">Email address</label>
                        <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" v-model="email">
                        <div id="emailHelp" class="form-text">*</div>
                    </div>
                    <div class="mb-3">
                        <label for="exampleInputPassword1" class="form-label">Password</label>
                        <input type="password" class="form-control" id="exampleInputPassword1" v-model="password" @input = "validatePassword" >
                        <div id="passwordHelp" class="form-text">*</div>
                        <div id="passwordHelp" class="form-text">{{ passwordError }}</div>
                    </div>
                    <div class="mb-3">
                        <label for="exampleInputName" class="form-label">Enter your name</label>
                        <input type="text" class="form-control" id="exampleInputname" aria-describedby="nameHelp" v-model="name">
                        <div id="name" class="form-text">*</div>
                    </div>
                    <div class="mb-3">
                        <label for="exampleInputName" class="form-label">Enter Qualification</label>
                        <input type="text" class="form-control" id="exampleInputname" aria-describedby="nameHelp" v-model="qualification">
                        <div id="name" class="form-text">*</div>
                    </div>
                    <div class = "mb-3">
                        <label class="form-label">Your specialization</label>
                        <select class="form-select" v-model="specialization">
                            <option value="">Select Specialization</option>
                            <option>Cardiologist</option>
                            <option>Neurologist</option>
                            <option>Orthopedic</option>
                            <option>Dermatologist</option>
                        </select>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">Years of Experience</label>
                        <input type="number" class="form-control" v-model="experience_year" min="0">
                    </div>
                    <button type="submit" class="btn btn-primary">Submit</button>
                    <button type="button" class="btn btn-outline-dark" @click ='Back'>Back</button>
      
                </form>
            </div>

        </div>
    </div>
</template>