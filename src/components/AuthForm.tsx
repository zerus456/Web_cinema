import { useState } from "react";
import ShowHidePassword from "./ShowHidePassword";
import Calendar from "./Calendar";

export default function AuthForm() {
  const [tab, setTab] = useState<"signin" | "signup">("signin");

  return (
    <div className="bg-[#FDFCF0] px-40">
      <div className="bg-white border rounded-[10px] p-8 w-[450px] my-12">
        {/* Tab */}
        <div className="flex justify-center mb-6 gap-18">
          <button
            onClick={() => setTab("signin")}
            className={`px-6 py-2 h-14 w-38 rounded-[10px] font-semibold duration-75 ease-in-out ${
              tab === "signin"
                ? "bg-[#FFE507] border border-black"
                : "hover:bg-[#F5F5F0] cursor-pointer duration-150 ease-in-out"
            }`}
          >
            SIGN IN
          </button>
          <button
            onClick={() => setTab("signup")}
            className={`px-6 py-2 h-14 w-38 rounded-[10px] font-semibold duration-75 ease-in-out ${
              tab === "signup"
                ? "bg-[#FFE507] border border-black"
                : "hover:bg-[#F5F5F0] cursor-pointer duration-150 ease-in-out"
            }`}
          >
            SIGN UP
          </button>
        </div>

        {/* Sign in From */}
        {tab === "signin" && (
          <form className="space-y-4 duration-75 ease-in-out">
            {/* Username, email box */}
            <div>
              <label className="block font-medium mb-2">
                Email, username <span className="text-red-600">*</span>
              </label>
              <input
                type="text"
                className="w-full h-12 border rounded-[10px] px-3 py-2 hover:outline outline-auto duration-85 ease-in-out"
                placeholder="Enter email or username"
              />
            </div>

            {/* Password */}
            <div>
              <label className="block font-medium mb-2">
                Password <span className="text-red-600">*</span>
              </label>
              <ShowHidePassword placeholder="Password" />
            </div>

            {/* Forgot password */}
            <div>
              <a
                href="#"
                className="flex justify-end font-medium underline mt-8"
              >
                Forgot password?
              </a>
            </div>

            {/* Sign in Button */}
            <div>
              <button className="w-full h-12 font-semibold border rounded-[10px] bg-[#FFE99A] hover:bg-[#FFD586] cursor-pointer duration-85 ease-in-out">
                SIGN IN
              </button>
            </div>
          </form>
        )}

        {/* Sign up Form */}
        {tab === "signup" && (
          <form className="space-y-4 duration-75 ease-in-out">
            {/* Name */}
            <label className="block font-medium mb-2">
              Name (Last, first) <span className="text-red-600">*</span>
            </label>
            <input
              type="text"
              className="w-full h-12 border rounded-[10px] px-3 py-2 hover:outline outline-auto duration-85 ease-in-out"
              placeholder="Name"
            />

            {/* Birthday */}
            <label className="block font-medium mb-2">
              Birthday <span className="text-red-600">*</span>
            </label>
            <Calendar />

            {/* Email */}
            <label className="block font-medium mb-2">
              Email <span className="text-red-600">*</span>
            </label>
            <input
              type="text"
              className="w-full h-12 border rounded-[10px] px-3 py-2 hover:outline outline-auto duration-85 ease-in-out"
              placeholder="Email"
            />

            {/* Username */}
            <label className="block font-medium mb-2">
              Username <span className="text-red-600">*</span>
            </label>
            <input
              type="text"
              className="w-full h-12 border rounded-[10px] px-3 py-2 hover:outline outline-auto duration-85 ease-in-out"
              placeholder="Username"
            />

            {/* Password */}
            <label className="block font-medium mb-2">
              Password <span className="text-red-600">*</span>
            </label>
            <ShowHidePassword placeholder="Password" />

            {/* Confirm password */}
            <label className="block font-medium mb-2">
              Confirm password <span className="text-red-600">*</span>
            </label>
            <ShowHidePassword placeholder="Confirm password" />

            {/* Sign up Button */}
            <button className="w-full h-12 font-semibold border rounded-[10px] mt-8 bg-[#FFE99A] hover:bg-[#FFD586] cursor-pointer duration-85 ease-in-out">
              SIGN UP
            </button>
          </form>
        )}
      </div>
    </div>
  );
}
