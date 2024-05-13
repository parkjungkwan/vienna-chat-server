'use client'

import { useState } from "react";
import { SubmitHandler, useForm } from "react-hook-form";

export default function Home() {

  const [message, setMessage] = useState('')
  const [category, setCategory] = useState('')

  type Inputs = {
    question: string
    category: string
    exampleRequired?: string
  }

  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm<Inputs>()
  const onSubmit: SubmitHandler<Inputs> = (data) => {
    console.log("input qusetion: ", watch("question"))
    fetch('http://localhost:8000/api/chat/' + `${category}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data)
    })
      .then((response) => response.json())
      .then((data) => setMessage(data.answer))
      .catch((error) => console.log("error: ", error));
  }

  const handleRadio = (e: any) => {
    setCategory(e.target.value)
    console.log("select button : ", e.target.value)
  }

  return (
    <div className="w-screen h-screen">
      <div className="mt-[5%] ml-[5%] mr-[5%]">
        

        

        <div className="flex justify-start gap-8 inline-fle  text-center">
          <div className="Card w-[404px] h-[434px] flex-col justify-start items-center gap-6 inline-flex">
            <input type="image" onClick={handleRadio} value={"titanic"} className="Image w-[404px] h-[346px]  rounded-lg" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQXL7QuFPAtOQIiDsHM9eK32hJmHy-hCQ3cGA&s" />
            <div className="Copy self-stretch h-16 flex-col justify-center items-center gap-1 flex">
              {category === "titanic" ?
                <div>
                  <div className="Title self-stretch text-black text-xl font-medium font-['Inter'] leading-[30px]">titanic</div>
                  <div className="Author self-stretch text-zinc-500 text-xl font-medium font-['Inter'] leading-[30px]">titanic</div>
                </div> :
                <div className="blur-sm">
                  <div className="Title self-stretch text-black text-xl font-medium font-['Inter'] leading-[30px]">titanic</div>
                  <div className="Author self-stretch text-zinc-500 text-xl font-medium font-['Inter'] leading-[30px]">titanic</div>
                </div>
              }
            </div>
          </div>

          <div className="Card w-[404px] h-[434px] flex-col justify-start items-center gap-6 inline-flex">
            <input type="image" onClick={handleRadio} value={"newone"} className="Image w-[404px] h-[346px]  rounded-lg" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRo7frHxpAeNlQhhLF5KCS1fcz4kbJet-OvoQ&s" />
            <div className="Copy self-stretch h-16 flex-col justify-center items-center gap-1 flex">
              {category === "newone" ?
                <div>
                  <div className="Title self-stretch text-black text-xl font-medium font-['Inter'] leading-[30px]">newone</div>
                  <div className="Author self-stretch text-zinc-500 text-xl font-medium font-['Inter'] leading-[30px]">newone</div>
                </div> :
                <div className="blur-sm">
                  <div className="Title self-stretch text-black text-xl font-medium font-['Inter'] leading-[30px]">newone</div>
                  <div className="Author self-stretch text-zinc-500 text-xl font-medium font-['Inter'] leading-[30px]">newone</div>
                </div>
              }
            </div>
          </div>

          <div className="Card w-[404px] h-[434px] flex-col justify-start items-center gap-6 inline-flex">
            <input type="image" onClick={handleRadio} value={"newone2"} className="Image w-[404px] h-[346px]  rounded-lg" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQbcaAuLQbW2Nobxavn2TZn3ffD6s_u_DUfw&s" />
            <div className="Copy self-stretch h-16 flex-col justify-center items-center gap-1 flex">
              {category === "newone2" ?
                <div>
                  <div className="Title self-stretch text-black text-xl font-medium font-['Inter'] leading-[30px]">newone2</div>
                  <div className="Author self-stretch text-zinc-500 text-xl font-medium font-['Inter'] leading-[30px]">newone2</div>
                </div> :
                <div className="blur-sm">
                  <div className="Title self-stretch text-black text-xl font-medium font-['Inter'] leading-[30px]">newone2</div>
                  <div className="Author self-stretch text-zinc-500 text-xl font-medium font-['Inter'] leading-[30px]">newone2</div>
                </div>
              }
            </div>
          </div>
         


        </div>
        <form onSubmit={handleSubmit(onSubmit)} >
          <div className="self-stretch text-black text-[64px] font-bold font-['Inter']">Titanic에 대해서 물어보세요!</div>

          <div className="flex justify-start min-h-full rounded-xl h-20 mb-5">

            <input className="w-[95%] rounded-xl border " type="sumit" placeholder="      Message ChatGPT" {...register("question", { required: true })} />
            {/* <button className="bg-gray-100 rounded-xl w-[5%] border" type="submit">input!</button> */}
          </div>
        </form >
        <div className="text-xl mt-5 text-[23px] rounded-t-lg bg-gray-100 shadow-xl shadow-gray-500">
              {message ? <p className="w-full mx-8"> {message} </p>
              :
              <p className="animate-bounce opacity-50 text-[50px] text-center">Wait . . .</p>
              }
          </div>

      </div>
    </div>

  );
}