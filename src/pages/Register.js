import React, { useEffect, useState } from 'react'
import axios from 'axios'

function Register() {
    
    const [data, setData] = useState({username:'',email:'', password:''})
    const[successMessage, setSuccessMessage] = useState('')

    
    const handleSubmit = async (e) =>{
        e.preventDefault()
        try {
            const response = await axios.post('http://localhost:8000/api/register/', data);
            setSuccessMessage("Registration successful please login!")
            setData({username:'', email:'', password:''})
        } catch (error) {
            console.error('error', error)
            setSuccessMessage('Registration failed!')
        }
    }
    

    const handleChange = (e) => {
        const {name, value } = e.target;
        setData((data) =>({...data,[name]:value}))
    }


  return (
    <div>
       <form onSubmit={handleSubmit}>
       <input type='text' name='username' placeholder='username' value={data.username} onChange={handleChange}/>
       <input type='email' name='email' placeholder='email' value={data.email} onChange={handleChange}/>
       <input type='password' name='password' placeholder='password' value={data.password} onChange={handleChange}/>
       <button type='submit'>Submit</button>
       </form>
        {successMessage && <p>{successMessage}</p>}

    </div>
  )
}

export default Register