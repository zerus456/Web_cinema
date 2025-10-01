import "./App.css";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import AuthForm from "./components/AuthForm";

function App() {
  return (
    <div className="flex flex-col min-h-screen">
      <Navbar />
      <main className="flex-1 bg-[#FDFCF0]">
        <AuthForm />
      </main>
      <Footer />
    </div>
  );
}

export default App;
