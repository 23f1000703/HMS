<script setup>
    import { ref } from 'vue';
    import { useRouter } from 'vue-router'

    const router = useRouter()

    const email = ref('');
    const password = ref('');

    const passwordError = ref('')
    

    const validatePassword = () => {
        if (password.value.length < 8){
            passwordError.value ='Your password length must be 8'
            return false
        } 
        else {
            passwordError.value = '';
            return true
        }

    }

    async function login(){
        if (!validatePassword()){
            alert("Invalid password length");
            return
        }
        if (email.value == ""|| password.value == ""){
            alert("please fill Email and Password")
            return
        }

        const user = {
            email : email.value,
            password : password.value
        }

        const response = await fetch('http://127.0.0.1:5000/api/login',{
            method: 'POST',
            headers:{
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(user)
        });
        console.log(response)

        

        if (!response.ok){
            const errordata = await response.json();
            console.error(errordata)
            alert(`Login failed: ${errordata.message}`);
            return;
        }
        else{
            const data = await response.json();
            console.log(data)
            
            localStorage.setItem('user_id',data.user_details.user_id)
            localStorage.setItem('token',data.user_details.auth_token)
            localStorage.setItem('role',data.user_details.roles[0])
            
            // localStorage.removeItem('token')
            alert(data.message)

            const role = data.user_details.roles[0] 

            if (role === 'admin') {
            router.push('/admin')
            }
            else if (role === 'patient'){
                router.push('/patient')
            }
            else if (role ==='doctor'){
                router.push('/doctor')
            }
            else{
                console.log("invalid role")
            }
            
            }

        } 
    
    
</script>



<template>
    <div class="container-fluid">
        <div class = "row justify-content-center mt-3">
            <div class = "col-6 align-items-center">
                <h1 class = text-center>Login</h1>
                <form @submit.prevent = "login">
                    <div class="mb-3">
                        <label for="exampleInputEmail1" class="form-label">Email address</label>
                        <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" v-model="email">
                        <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
                    </div>
                    <div class="mb-3">
                        <label for="exampleInputPassword1" class="form-label">Password</label>
                        <input type="password" class="form-control" id="exampleInputPassword1" v-model="password" @input = "validatePassword">
                        <div id="passwordHelp" class="form-text">{{ passwordError }}</div>
                    </div>
                    <button type="submit" class="btn btn-primary">Submit</button>
                </form>
            </div>

        </div>
    </div>
</template>

