#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "Solver.hpp"
#include "Position.hpp"


namespace py = pybind11;
using namespace GameSolver::Connect4;

PYBIND11_MODULE(perfect_player, m) {
    py::class_<Solver>(m, "Solver")
        .def(py::init<>())
        .def("solve", &Solver::solve)
        .def("loadBook", &Solver::loadBook);

	py::class_<Position>(m, "Position")
	    .def(py::init<>())
	    .def("play", py::overload_cast<std::string>(&Position::play))   
	    .def("playCol", &Position::playCol)
	    .def("canPlay",&Position::canPlay)   
	    .def("nbMoves",&Position::nbMoves)   
	    .def("isWinningMove",&Position::isWinningMove)  
	    .def_property_readonly_static("MIN_SCORE",[](py::object) { return Position::MIN_SCORE; })
	    .def_property_readonly_static("MAX_SCORE",[](py::object) { return Position::MAX_SCORE; }) 
	    .def_property_readonly_static("WIDTH",[](py::object) { return Position::WIDTH; }) 
	    .def_property_readonly_static("HEIGHT",[](py::object) { return Position::HEIGHT; }); 
}