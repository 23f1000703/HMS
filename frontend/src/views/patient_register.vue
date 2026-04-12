<script setup>
    import { useRouter } from 'vue-router'
    const router = useRouter()
    import { ref } from 'vue';

     const email = ref('');
     const password = ref('');
     const name = ref ('');
     const phone_no = ref('');
     const dob = ref ('');
     const gender = ref('');
     const blood_group = ref('');
     const address = ref('');


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
        if (name.value == "" || dob.value == "" || gender.value =="" || address.value == ""){
            alert("Please fill all * field")
            return
        }
        const user = {
            email : email.value,
            password : password.value,
            role: 'patient',
            name:name.value,
            phone_no:phone_no.value,
            dob: dob.value,
            gender: gender.value,
            blood_group: blood_group.value,
            address: address.value
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
            alert(`registration failed:${errordata.message}`)
            return
        }
    alert("Successfully register")
    router.push('/login')

    }
</script>

<template>
     <div class="container-fluid">
        <div class = "row justify-content-center mt-3">
            <div class = "col-6 align-items-center">
                <h1 class = text-center>Patient Registration</h1>
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
                        <label for="exampleInputName" class="form-label">Enter Your Name</label>
                        <input type="text" class="form-control" id="exampleInputName"  v-model="name">
                        <div id="emailHelp" class="form-text">*</div>
                    </div>
                    <div class="mb-3">
                        <label for="exampleInputName" class="form-label">Enter Phone num.</label>
                        <input type="tel" class="form-control" id="exampleInputName"  v-model="phone_no">
                        <div id="noHelp" class="form-text">*</div>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">Date of Birth</label>
                        <input type="date" class="form-control" v-model="dob">
                        <div id="dateHelp" class="form-text">*</div>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">Gender</label>
                        <select class="form-select" v-model="gender">
                            <option value="">Select Gender</option>
                            <option value="Male">Male</option>
                            <option value="Female">Female</option>
                            <option value="Other">Other</option>
                        </select>
                        <div id="genderHelp" class="form-text">*</div>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">Blood Group</label>
                        <select class="form-select" v-model="blood_group">
                            <option value="">Select Blood Group</option>
                            <option>A+</option>
                            <option>A-</option>
                            <option>B+</option>
                            <option>B-</option>
                            <option>O+</option>
                            <option>O-</option>
                            <option>AB+</option>
                            <option>AB-</option>
                        </select>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">Address</label>
                        <textarea class="form-control" rows="3" v-model="address"></textarea>
                        <div id="addressHelp" class="form-text">*</div>
                    </div>
                    
                    <button type="submit" class="btn btn-primary">Submit</button>
                </form>
            </div>

        </div>
    </div>
</template>

<style scoped>
/* CENTER CARD */
.col-6 {
  background: #ffffff;
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
}

/* FORM GRID */
form {
  display: grid;
  grid-template-columns: 1fr 1fr;  /* 2 columns */
  gap: 15px;
}

/* FULL WIDTH ELEMENTS */
form .mb-3:nth-child(7),
form .mb-3:nth-child(8) {
  grid-column: span 2;   /* Blood group + address full width */
}

/* BUTTON FULL WIDTH */
button {
  grid-column: span 2;
}

/* HEADING CENTER */
h1 {
  text-align: center;
  margin-bottom: 20px;
  font-weight: 600;
  color: #1e293b;
}

/* INPUT STYLING */
.form-control,
.form-select,
textarea {
  border-radius: 8px;
  padding: 8px;
  font-size: 14px;
  border: 1px solid #cbd5e1;
}

/* FOCUS */
.form-control:focus,
.form-select:focus,
textarea:focus {
  border-color: #38bdf8;
  box-shadow: 0 0 4px rgba(56, 189, 248, 0.4);
}

/* BUTTON */
.btn-primary {
  width: 100%;
  padding: 10px;
  border-radius: 8px;
  background: #38bdf8;
  border: none;
}

.btn-primary:hover {
  background: #0ea5e9;
}
</style>